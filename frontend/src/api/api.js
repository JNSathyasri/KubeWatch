import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:5000/api",
  timeout: 10000,
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error);

    if (error.response) {
      console.error("Status:", error.response.status);
    }

    return Promise.reject(error);
  }
);

export default api;