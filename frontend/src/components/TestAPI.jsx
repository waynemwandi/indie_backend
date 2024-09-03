import { useEffect, useState } from "react";

function TestAPI() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/daraja/test-api/")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
      })
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
