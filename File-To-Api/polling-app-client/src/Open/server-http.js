import axios from "axios";

export default axios.create({
  baseURL: "http://localhost:10005",
  headers: {
    "Content-type": "application/json"
  }
});
