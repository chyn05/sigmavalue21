import axios from "axios";

// Default for local development (npm run dev)
let BASE_URL = "http://127.0.0.1:8000/api";

// If Vite env variable is set, use that (optional)
if (import.meta.env.VITE_API_BASE_URL) {
  BASE_URL = import.meta.env.VITE_API_BASE_URL;
}

// If running on a deployed frontend (e.g. Vercel), force using Render backend URL
if (typeof window !== "undefined" && window.location.hostname.endsWith("vercel.app")) {
  // 🔴 IMPORTANT: change this to your actual Render backend URL
  BASE_URL = "https://sigmavalue21.onrender.com";
}

console.log("Using API base URL:", BASE_URL);

const api = axios.create({
  baseURL: BASE_URL,
});

export const analyzeQuery = async (query) => {
  const res = await api.post("/analyze/", { query });
  return res.data;
};
