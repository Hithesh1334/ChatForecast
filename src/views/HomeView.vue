<!-- src/components/MyComponent.vue -->
<script >

export default {
  data() {
    return {
      time: ""
    }
  },
  mounted() {
    const displayCurrentTime = () =>{
      const now = new Date();
      const currentTime = now.toLocaleTimeString();
      currentTime.toUpperCase();
      
      this.time = currentTime;
    }

    // Call the function initially
    displayCurrentTime();

    // Update the time every second
    setInterval(displayCurrentTime, 1000);
  }
}

</script>
<template>
  <main >
    <div class="flex flex-col justify-center items-center   p-8  mx-40  relative top-20">
      <h1 class=" text-8xl font-semibold text-gray-300 mb-4">Welcome to ChatForecast</h1>
      <p class="welcome text-2xl text-gray-400 mb-6">Your reliable companion for accurate weather forecasts.</p>
    </div>
    
    <div class="relative top-20 flex mx-40 justify-around items-center">
      <h1 class="text-slate-300 text-8xl p-7 border-double border-4 border-sky-300 shadow-xl shadow-sky-700 ">{{ time }}</h1>
      <img src="./images/weather.svg" width="400" height="400" alt="img"/>
    </div>
    <div class="relative top-20 mt-10 flex mx-40 justify-start">
      <RouterLink dir="rtl" class="bg-indigo-600 p-3 rounded-s-lg text-2xl hover:bg-indigo-400 text-slate-300"  to="/Chat">!Chat with weather</RouterLink>
    </div>
    <hr class="relative top-40 mx-40">
    <div class="relative top-40 mx-40">
      <p class="text-slate-300">@2023</p>
    </div>
  </main>
</template>
