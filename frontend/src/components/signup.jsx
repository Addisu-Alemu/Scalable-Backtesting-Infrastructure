import './signup.css'

import React from 'react';
import { Link } from 'react-router-dom';
function Signup() {

  return (
    <>
      <div class="container">
        <div class="wrapper">
          <div class="title">
            <span> Signup Form </span>
          </div>
          <form action="#">
            <div class="row">
              <i class="fas fa-user"></i>
              <input type="text" placeholder="Full Name" required />
            </div>
            <div class="row">
              <i class="fas fa-envelope"></i>
              <input type="email" placeholder="Email" required />
            </div>
            <div class="row">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Password" required />
            </div>
            <div class="row">
              <i class="fas fa-lock"></i>
              <input type="password" placeholder="Confirm Password" required />
            </div>
            <div class="pass">
              <a href="#">Forgot password?</a>
            </div>
            <div class="row button">
              <input type="submit" value="Signup" />
            </div>
            <button class="login-link">
              Already a member? <Link to="/">Signin</Link>
            </button>
          </form>
        </div>
      </div>
    </>
  );
}

export default Signup;