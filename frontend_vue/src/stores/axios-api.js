import axios from "axios";
import { userAuthStore } from "./authStore";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/",
  timeout: "9000",
});

api.interceptors.request.use(async (config) => {
  const authStore = userAuthStore();
  config.headers['Authorization'] = `Bearer ${authStore.accessToken}`
  return config
}, (error)=>{
  return Promise.reject(error)
});

export default api;
