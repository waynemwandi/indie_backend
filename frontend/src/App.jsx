import "./App.css";
import { useState } from "react";
import TestAPI from "./components/TestAPI.jsx";
import DarajaAPI from "./components/DarajaAPI.jsx";

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
      <DarajaAPI />
    </div>
  );
}

export default App;
