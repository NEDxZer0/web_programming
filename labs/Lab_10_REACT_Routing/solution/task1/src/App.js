import { Routes, Route, Link } from 'react-router-dom'
import Main from './Pages/Main'
import About from './Pages/About'
import NotFound from './Pages/NotFound'


function App() {
  return (
    <>
      <header >
        <Link to="/" style={{margin:30, fontSize:20}}>main</Link>
        <Link to="/about" style={{margin:30, fontSize:20}}>about</Link>
      </header>
      <Routes>
        <Route path='/' element={<Main/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='*' element={<NotFound/>}/>
      </Routes>
    </>
  );
}

export default App;