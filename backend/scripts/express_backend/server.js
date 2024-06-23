const express = require("express");
const cors = require("cors");
const { Pool } = require('pg');


const pool = new Pool({
    user: 'postgres',
    host: 'localhost',
    database: 'postgres',
    password: 'postgres',
    port: 5432,
  });


const app = express()
app.use(cors())

app.get('/', (req,res)=>{
     return res.json("From backend side");
})
app.get('/users', (req,res)=>{
    const psql = "SELECT * FROM users";
pool.query(psql, (err, data)=>{
    if(err) return res.json(err);
    return res.json(data.rows[0]);
})

})


app.listen(8081, ()=>{
    console.log("port is listening");
})
