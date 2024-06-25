import './login.css'
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  useEffect(() => {
    // Retrieve the last entered email from localStorage when the component mounts
    const lastEmail = localStorage.getItem('lastEmail');
    if (lastEmail) {
      setEmail(lastEmail);
    }
  }, []);

  function handleSubmit(event) {
    event.preventDefault();
    
    // Save the current email to localStorage
    localStorage.setItem('lastEmail', email);
    
    // Your login logic here
    console.log("Login attempt with:", email, password);
  }

  return (
    <>
      <div className="container">
        <div className="wrapper">
          <div className="title">
            <span> Login Form </span>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="row">
              <i className="fas fa-user"></i>
              <input 
                type="text" 
                placeholder="Email" 
                required 
                value={email}
                onChange={e => setEmail(e.target.value)}
              />
            </div>
            <div className="row">
              <i className="fas fa-lock"></i>
              <input 
                type="password" 
                placeholder="Password" 
                required 
                value={password}
                onChange={e => setPassword(e.target.value)}
              />
            </div>
            <div className="pass">
              <a href="#">Forgot password?</a>
            </div>
            <div className="row button">
              <button type="submit" className="signup-link"><Link to="/input">Login</Link></button>
            </div>
            <button type="button" className="signup-link">
              Not a member? <Link to="/signup">Signup</Link>
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

export default Login;