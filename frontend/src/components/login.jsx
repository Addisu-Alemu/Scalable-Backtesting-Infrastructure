import './login.css'
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
function Login() {

const[email, setEmail] = useState("")
const[password, setPassword] = useState("")
function handleSubmit(event){
  event.preventDefault();
  
}

  return (
    <>
      <div class="container">
        <div class="wrapper">
          <div class="title">
            <span> Login Form </span>
          </div>
          <form onSubmit={handleSubmit}>
            <div class="row">
              <i class="fas fa-user"></i>
              <input type="text " placeholder="Email" required onChange={e => {setEmail(e.target.value)}}/>
            </div>
            <div class="row">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Password" required onChange={e => {setPassword(e.target.value)}}/>
            </div>
            <div class="pass">
              <a href="#">Forgot password?</a>
            </div>
            <div class="row button">
              <input type="submit" value="Login" />
            </div>
            <button class="signup-link">
              Not a member? <Link to="/signup">Signup</Link>
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

export default Login;