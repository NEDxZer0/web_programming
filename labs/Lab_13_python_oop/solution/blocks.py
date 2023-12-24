from datetime import datetime 

from base import BaseBlock


class ParametrsBlock(BaseBlock):
    NAME = 'Аналитика платежей'
    DATE = 'Дата анализа'
    PERIOD = 'Период выгрузки'

    def wr_header(self):
        self.ws.write(self.row,self.col,self.NAME)
    
    def wr_data(self):
        self.row+=1
        self.ws.write(self.row,self.col,self.DATE)

        self.col+=1
        date = datetime.now().strftime('%d.%m.%Y') 
        self.ws.write(self.row,self.col,date)

        self.col-=1
        self.row+=1
        self.ws.write(self.row,self.col,self.PERIOD)

        self.col+=1
        dates = [payment['created_at'] for payment in self.data['payments']]
        dates = [datetime.fromisoformat(date[:-1]) for date in dates]
        dates.sort()
        date_low_str = dates[0].strftime('%d-%m-%Y')
        date_upp_str = dates[-1].strftime('%d-%m-%Y')
        date = f'{date_low_str} - {date_upp_str}'
        self.ws.write(self.row,self.col,date)

        self.col=0
        self.row+=2


class PayersBlock(BaseBlock):
    #NAME = 'Активность клие'
    TOP = 'Топ 10 клиентов'
    
    def wr_header(self):
        self.row=4
        self.col=0
        #self.ws.write(self.row,self.col,self.NAME)
        #self.row+=1
        self.ws.merge_range('A5:F5',self.TOP)
        self.row+=1

    def wr_data(self):
        clients_payments = []
        for client in self.data['clients']:
            for payment in self.data['payments']:
                if client['id'] == payment['client_id']:
                    clients_payments.append({
                        'fio': client['fio'],
                        'payment_amount': payment['amount'],
                        'payment_created_at': payment['created_at']
                    })

        clients_payments.sort(key=lambda x: datetime.fromisoformat(x['payment_created_at']),reverse=True)

        quarters = {}
        for client_payment in clients_payments:
            payment_date = datetime.fromisoformat(client_payment['payment_created_at'])
            q = f'Q{(payment_date.month%4 + 1)} {payment_date.year}' 
            quarters.setdefault(q,[]).append({
                'fio':client_payment['fio'],
                'payment_amount':client_payment['payment_amount']
                })

        for q in quarters:
            self.ws.write(self.row,self.col,q)
            srt = sorted(quarters[q], key=lambda x:x['payment_amount'])[:10]
            for s in srt:
                self.row+=1
                self.ws.write(self.row,self.col,s['fio'])
            self.row-=10
            self.col+=1
                

class GeographyBlock(BaseBlock):
    #NAME = 'ГЕОГРАФИЯ КЛИЕНТОВ'
    STATISTIC = 'Статистика распределения клиентов'
    CITY = 'Города'
    AMOUNT = 'Kоличество клиентов'

    def wr_header(self):
        self.col=0
        self.row=18
        #self.ws.write(self.row,self.col,self.NAME)
        #self.row+=1
        self.ws.merge_range('A19:C19',self.STATISTIC)
        self.row+=1
        self.ws.write(self.row,self.col,self.CITY)
        self.col+=1
        self.ws.write(self.row,self.col,self.AMOUNT)
        self.col=1
        self.row+=1

    def wr_data(self):
        cities={}
        for client in self.data['clients']:
            city = client['city']
            if city in cities:
                cities[city]+=1
            else: 
                cities[city]=1
        
        sort_cities = sorted(cities.items(), key=lambda x: x[1], reverse=True)
        
        for city, count in sort_cities[:10]:
            self.ws.write(self.row,self.col,city)
            self.col+=1
            self.ws.write(self.row,self.col,count)#на 30й строке
            self.col-=1
            self.row+=1


class StatusBlock(BaseBlock):
    #NAME = 'АНАЛИЗ СОСТОЯНИЯ СЧЕТА'
    STATISTIC = 'Статистика состояния счета'
    CLIENT = 'Клиент'
    STATE = 'Состояние счета'
    DEBT = 'Задолженность'
    PROFIT = 'Прибыль'

    def wr_header(self):
        self.col=0
        self.row=32
        #self.ws.write(self.row,self.col,self.NAME)
        self.ws.merge_range('A33:D33',self.STATISTIC)
        self.ws.merge_range('A35:B35',self.DEBT)
        self.ws.merge_range('C35:D35',self.PROFIT)
        self.row+=1
        self.ws.write(self.row,self.col,self.CLIENT)
        self.col+=1
        self.ws.write(self.row,self.col,self.STATE)
        self.col+=1
        self.ws.write(self.row,self.col,self.CLIENT)
        self.col+=1
        self.ws.write(self.row,self.col,self.STATE)
    
    def wr_data(self):
        self.col=0
        self.row=35

        status = []
        for client in self.data['clients']:
            for payment in self.data['payments']:
                if client['id'] == payment['client_id']:
                    status.append({
                        'fio': client['fio'],
                        'payment_amount': payment['amount'],
                    })
        
        status.sort(key=lambda x:x['payment_amount'],reverse=True)

        for s in status[-10:]:
            self.ws.write(self.row,self.col,s['fio'])
            self.col+=1
            self.ws.write(self.row,self.col,s['payment_amount'])
            self.col-=1
            self.row+=1
        
        self.col=2
        self.row=35

        for s in status[:10]:
            self.ws.write(self.row,self.col,s['fio'])
            self.col+=1
            self.ws.write(self.row,self.col,s['payment_amount'])
            self.col-=1
            self.row+=1