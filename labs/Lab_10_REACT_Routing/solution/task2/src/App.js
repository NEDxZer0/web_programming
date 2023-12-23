import { Routes, Route } from 'react-router-dom'
import Main from './Pages/Main'
import About from './Pages/About'
import NotFound from './Pages/NotFound'
import { useState } from 'react'


function App() {
  const [users, setUsers]=useState([]);
  const Fetch = ()=>{
    fetch('https://swapi.dev/api/people/')
    .then(response => {
      if (response.ok) {
          return response.json();
      } else {
          throw new Error('Error receiving data: ' + response.status);
      }
    })
    .then(data => {
      setUsers(data.results.map(person => {
        return {
            name: person.name,
            birth_year: person.birth_year,
            id: person.created
        };
      }));
      console.log(data.results)
    })
    .catch(error => {
        console.log(error);
    });
  }


  return (
    <>
      <button onClick={Fetch} style={{margin:30,marginBottom:0,fontSize:15,padding:10}}>Upload data</button>
      <Routes>
        <Route path='/' element={<Main users={users}/>}/>
        <Route path='/about/:id' element={<About users={users}/>}/>
        <Route path='*' element={<NotFound/>}/>
      </Routes>
    </>
  );
}

export default App;