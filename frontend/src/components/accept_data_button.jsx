import React, { useState, useEffect } from "react";

function Accept() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleClick = () => {
    setLoading(true);
    fetch("http://localhost:8081/users")
      .then((res) => res.json())
      .then((data) => setData([data]))
      .finally(() => setLoading(false));
  };

  return (
    <div style={{padding:'50px'}}>
      <button onClick={handleClick}>Load Data</button>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>NAME</th>
            <th>EMAIL</th>
          </tr>
        </thead>
        <tbody>
          {data.map((d, i) => (
            <tr key={i}>
              <td>{d.id}</td>
              <td>{d.name}</td>
              <td>{d.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    
    </div>
  );
}

export default Accept;