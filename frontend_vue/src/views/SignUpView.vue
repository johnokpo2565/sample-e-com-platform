<template>
    <div class="row mt-4 mx-auto">
        <div class="row mx-auto w-25">
            <div class="">
                <h4>Sign Up</h4>
            </div>
            <input v-model="email" type="text" class="form-control" placeholder="Enter Username/email" >
            <input v-model="password" type="password" class="form-control mt-2" placeholder="Enter Password">
            <button type="password" class="btn btn-sm btn-danger w-50 mt-3" >Login</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
const email = ref('')
const password = ref('') 
</script>
