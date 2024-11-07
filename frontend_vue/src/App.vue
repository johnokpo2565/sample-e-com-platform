<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import NavBar from './components/NavBar.vue';
</script>

<template>
  <header>
    
    <div class="wrapper">
     

      <nav>
        <NavBar/>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
