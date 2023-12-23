import React from "react";
import {Link} from 'react-router-dom'

function Main({ users }) {
  return (
    <>
      <h1 style={{fontSize:40, margin:25}}>Users:</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            <Link to={`/about/${user.id}`} style={{fontSize:20}}>{user.name}</Link>
          </li>
        ))}
      </ul>
    </>
  );
}

export default Main;