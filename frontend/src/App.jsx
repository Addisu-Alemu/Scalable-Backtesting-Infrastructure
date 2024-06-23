import "./App.css";
import Accept from "./components/accept_data_button";
import Login from "./components/login";
import Signup from "./components/signup";


function App() {
  return (
    <>

{/* <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="signup" element={<Signup />} />
      </Routes>
    </BrowserRouter> */}
    <Accept />
    </>
  );
}

export default App;
