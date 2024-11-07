<template>
    <div class="row mt-4 mx-auto">
        <div class="row mx-auto w-25 my-4">
            <div class="">
                {{ userdetails }}
                <h4>Dashboard, {{ username }}</h4>
            </div>

            <div class="row my-2">
                <input v-model="email" class="form-control my-2" type="text" placeholder="Enter your email">
                <input v-model="amount" class="form-control my-2" type="number" placeholder="Enter your amount" >
                <!-- <input class="form-control my-2" type="text" placeholder="" > -->
            </div>

            <div class="row">
                <button class=" btn btn-sm btn-primary" @click="initializePayment">Initialize payment</button>
            </div>

            <!-- <div class="row mx-3">
                <button class="btn btn-sm btn-success" @click="handlePullRecords">Pull Records</button>
            </div> -->
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import api from '../stores/axios-api';
import Paystack from '@paystack/inline-js';
import {userAuthStore} from '../stores/authStore';
const authStore = userAuthStore()
const username = ref('John Doe') 
const userdetails = ref([])
const popup = new Paystack()
const amount = ref('')
const email = ref('')

const handlePullRecords = async() =>{
// Testing to see how I use api interceptor to add authorization header to my request so as I can access JWT secured endpoints
    try {
        const response = await api.get('/api/assets')
        console.log(response.data);
    } catch (error) {
        console.log(error)
    }
    
}

const initializePayment = () =>{
    const paymentResponse = authStore.initializePayment(email.value, amount.value)

    paymentResponse.then(res=>{
        if(res)
        {
            console.log(authStore.access_code);
        }
        else
        {
            
        }
        
    }).catch(error=>{
        console.log(error);
        
    })
    
}

onMounted(()=>{
    // Get user details from localstorage
    const storedUser = localStorage.getItem('user')    
   userdetails.value = JSON.parse(storedUser)
    
})

</script>
