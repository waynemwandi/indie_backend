// src/components/TestAPI.js
import { useState, useEffect } from "react";

function TestAPI() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/test-api/")
      .then((response) => response.json())
      .then((data) => setData(data))
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <div>
      <h1>Test API</h1>
      {data ? (
        <div>
          <p>Message: {data.message}</p>
          <p>Status: {data.status}</p>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default TestAPI;
