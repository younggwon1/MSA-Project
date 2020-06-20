
import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:10003",
  headers: {
    "Content-type": "application/json"
  }
});

// http://localhost:10003/start?user=userId