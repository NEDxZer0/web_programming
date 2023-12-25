import datetime
import json
import os

from writer import Writer

def load_data(file_name):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', file_name)

    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

def main():
    data_clients = load_data('clients.json')
    data_payments = load_data('payments.json')

    data = {'clients':data_clients['clients'], 'payments':data_payments['payments']}

    date = datetime.date.today().strftime('%Y_%m_%d')
    os.chdir('..')
    output_file = f'my_payments_analytics_{date}.xlsx'

    writer = Writer(data)   
    writer.write_excel(output_file)

if __name__ == '__main__':
    main()