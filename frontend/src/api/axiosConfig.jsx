import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/v2", // ton serveur Flask
  headers: {
    "Content-Type": "application/json"
  }
});

export default api;
