import axios from "axios";

const BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api";

const api = axios.create({
  baseURL: BASE_URL,
});

export const analyzeQuery = async (query) => {
  const res = await api.post("/analyze/", { query });
  return res.data;
};
