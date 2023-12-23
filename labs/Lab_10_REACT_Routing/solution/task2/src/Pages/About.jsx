import React from 'react'
import { useParams } from 'react-router-dom'

function About({users}) {
  const { id } = useParams();

  const user = users.find((u) => u.id === id);

  if (!user) {
    return <div>User not found</div>;
  }

  return (
    <div>
      <h2 style={{fontSize:30,  marginBottom:10, marginTop:20, marginLeft:30}}>{user.name}</h2>
      <p style={{fontSize:20, marginBottom:15, marginTop:15, marginLeft:30}}>Birth_year: {user.birth_year}</p>
      <p style={{fontSize:20, marginBottom:15, marginTop:15, marginLeft:30}}>id: {user.id}</p>
    </div>
  );
}

export default About