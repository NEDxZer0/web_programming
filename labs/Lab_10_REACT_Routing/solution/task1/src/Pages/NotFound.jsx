import React from 'react'
import {Link} from 'react-router-dom'

function NotFound() {
  return (
    <div style={{margin:30,fontSize:30}}>Page not found. 
    <br></br>  return to <Link to='/'>main</Link></div>
  )
}

export default NotFound