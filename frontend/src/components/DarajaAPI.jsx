import { useEffect, useState } from "react";
import axios from "axios";

const DarajaAPI = () => {
  const [payments, setPayments] = useState([]);

  useEffect(() => {
    const fetchPayments = async () => {
      try {
        const response = await axios.get("/api/daraja/payments/");
        console.log(response.data);
        setPayments(response.data);
      } catch (error) {
        console.error("There was an error fetching the payments!", error);
      }
    };

    fetchPayments();
  }, []);

  return (
    <div>
      <h1>Payments</h1>
      <table border="1">
        <thead>
          <tr>
            <th>ID</th>
            <th>Transaction ID</th>
            <th>Amount</th>
            <th>Phone Number</th>
            <th>Transaction Time</th>
          </tr>
        </thead>
        <tbody>
          {Array.isArray(payments) &&
            payments.map((payment) => (
              <tr key={payment.id}>
                <td>{payment.id}</td>
                <td>{payment.trans_id}</td>
                <td>{payment.trans_amount}</td>
                <td>{payment.msisdn}</td>
                <td>{new Date(payment.trans_time).toLocaleString()}</td>
              </tr>
            ))}
        </tbody>
      </table>
    </div>
  );
};

export default DarajaAPI;
