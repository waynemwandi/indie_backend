import "./App.css";
import { useState } from "react";
// import reactLogo from "./assets/react.svg";
// import viteLogo from "/vite.svg";
import "./App.css";

// src/App.jsx
import TestAPI from "./components/TestAPI.jsx";

function App() {
  const [count, setCount] = useState(0);
  return (
    <div className="App">
      <h1>INDIE React App</h1>
      <>
        <h1>React + Django Microservices</h1>
        <div className="card">
          <button onClick={() => setCount((count) => count + 1)}>
            count is {count}
          </button>
        </div>
      </>
      <TestAPI />
    </div>
  );
}

export default App;
