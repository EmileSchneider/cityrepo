<template>
<div id="app">
  <b-container class="body">
    <div id="nav">
     <router-link :to="{ name: 'home' }">Me</router-link> |
     <router-link :to="{ name: 'portfolio' }">Portfolio</router-link> |
     <router-link :to="{ name: 'CV' }">CV</router-link>
    </div>
    <router-view/>
  </b-container>
  
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.body {
    background-color: whitesmoke;
}

</style>
