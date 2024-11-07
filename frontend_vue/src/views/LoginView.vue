<template>
    <div class="row mt-4 mx-auto">
        <div class="row mx-auto w-25">
            <div class="">
                <p v-if="incorrectAuth"> Incorrect user or password</p>
                <h4>Loginx</h4>
            </div>
            <input v-model="email" type="text" class="form-control" placeholder="Enter Username/email" >
            <input v-model="password" type="password" class="form-control mt-2" placeholder="Enter Password">
            <button class="btn btn-sm btn-danger w-50 mt-3" @click="login">Login</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { userAuthStore } from '../stores/authStore';
import { useRouter,useRoute } from 'vue-router';
// import api from '../store/axios-api';
const authStore = userAuthStore()
const accessToken = authStore.accessToken


const email = ref('')
const password = ref('')
const incorrectAuth = ref(false)
const router = useRouter() 

const login = () =>{

    const handle = authStore.login(email.value, password.value)
   handle.then(res=>{
    // console.log(res);
    
    if(res)
    {
        router.push('/dashboard')
        // console.log(authStore.isTokenExpired());
    }
    else{
        incorrectAuth.value = true
    }

   }
   ).catch(err=>{
    console.log(err)
   })
    // if(handle)
    // {
    //     // console.log("go to dashboard")
    //     // console.log(handle)
    //     // router.push('/dashboard')
    //     // window.location.href ='/dashboard'
    // }
    // else
    // {
    //     incorrectAuth.value=false
    // }
    // console.log(handle);
}

</script>
