import { ref, computed } from "vue";
import { defineStore } from "pinia";
// import { getAPI } from "./axios-api";
import axios from "axios";
// import * as jwt_decode from "jwt-decode";
// import jwt from 'jsonwebtoken';
// import { useJwt } from '@vueuse/integrations/useJwt'

export const userAuthStore = defineStore({
  id: "auth",
  state: () => ({
    // accessToken: "testing1",
    // refreshToken: "testing2",

    accessToken: localStorage.getItem("accessToken") || null,
    refreshToken: localStorage.getItem("refreshToken") || null,
    user: localStorage.getItem("user") || null,
    access_code: null,
  }),

  actions: {
    setTokens(accessToken, refreshToken, user) {
      this.accessToken = accessToken;
      this.refreshToken = refreshToken;
      this.user = user.data;
      localStorage.setItem("accessToken", accessToken);
      localStorage.setItem("refreshToken", refreshToken);
      localStorage.setItem("user", JSON.stringify(user));  //Stringifying user object array fetched from django backend
    },

    destoryTokens() {
      this.accessToken = null;
      this.refreshToken = null;
      this.refreshToken = null;
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
      localStorage.removeItem("user");
    },

    refreshTokenAccessToken(accessToken) {
      this.accessToken = accessToken;
    },

    isTokenExpired() {
      // if (this.accessToken) return true;
      // const decodeToken = jwt_decode(this.accessToken);
      // const currentTime = Date.now() / 1000;
      // return decodeToken.exp < currentTime;
      // console.log(jwt.decode(this.accessToken));
      return true
      
    },

    setAccessCode(access_code){
      this.access_code = access_code
    },

    async login(email, password) {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/auth/login/",
          {
            email: email,
            password: password,
          }
        );

        const { access, refresh, user } = response.data;
        this.setTokens(access, refresh, user);
        return true;
        // categories.value = response.data
        // console.log(`access: ${access}, refresh: ${refresh}`);
        // console.log(`${username} and ${password}`);
      } catch (error) {
        console.log("never", error);
        return false;
      }
    },


    async initializePayment(email, amount)
  {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/payment/initialize/', {
        email,
        amount
      })

      this.setAccessCode(response.data.access_code)
      return true
      // console.log(response);
      
    } catch (error) {
      console.log(error);
      return false
        
    }
  },

  },

  

  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },
});
