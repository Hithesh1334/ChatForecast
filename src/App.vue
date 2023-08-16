<template >
    <nav class="flex justify-center bg-slate-50 z-10 bg-opacity-5 rounded p-1 mx-40 right-0 left-0  backdrop-blur fixed">
    <router-link class="m-2 text-2xl" to="/"><img src="./assets/icons/home.png" height="40" width="40" alt="Home"/></router-link>
    <router-link class="m-2 text-2xl" to="/Docs"><img src="./assets/icons/code.png" height="40" width="40" alt="Home"/></router-link>
  </nav>
  <router-view/>

</template>

