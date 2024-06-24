import React, { useState } from "react";

function Send() {
  const [data, setData] = useState({
    id: "",
    name: "",
    email: ""
  });
  const [loading, setLoading] = useState(false);

  const handleClick = () => {
    setLoading(true);
    fetch("http://localhost:8081/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    })
      .then((res) => res.json())
      .then((result) => console.log(result))
      .finally(() => setLoading(false));
  };

  return (
    <div style={{ padding: "50px" }}>
      <form>
        <label>ID:</label>
        <input type="text" value={data.id} onChange={(e) => setData({ ...data, id: e.target.value })} />
        <br />
        <label>NAME:</label>
        <input type="text" value={data.name} onChange={(e) => setData({ ...data, name: e.target.value })} />
        <br />
        <label>EMAIL:</label>
        <input type="text" value={data.email} onChange={(e) => setData({ ...data, email: e.target.value })} />
        <br />
        <label>Password:</label>
        <input type="text" value={data.password} onChange={(e) => setData({ ...data, password: e.target.value })} />
        <br />
        <button onClick={handleClick}>Send Data</button>
      </form>
      {loading ? <p>Loading...</p> : <p>Data sent!</p>}
    </div>
  );
}

export default Send;