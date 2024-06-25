import "./App.css";
import Login from "./components/login";
import Signup from "./components/signup";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import User_input from "./components/user_input";

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="signup" element={<Signup />} />
          <Route path="input" element={<User_input />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
