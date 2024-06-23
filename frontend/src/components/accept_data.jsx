import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8081/users")
      .then((res) => res.json())
      .then((data) => setData(data));
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>NAME</th>
          <th>EMAIL</th>
        </tr>
      </thead>
      <tbody>
       
          <tr key={i}>
            <td>{d.id}</td>
            <td>{d.name}</td>
            <td>{d.email}</td>
          </tr>
        
      </tbody>
    </table>
  );
}

export default App;