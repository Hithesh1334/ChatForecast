<template>
    <main class="relative top-20">
        <div class="mx-40 text-gray-400">
           <h1 class="text-4xl text-slate-300  mb-3">ChatForecast</h1>
           <hr>
           <h1 class="text-4xl text-slate-300 mt-5">Overview</h1><hr class="border-t border-gray-500">
           <p class="text-justify">This application provides a convenient way for users to obtain weather forecasts for their location by inputting the name of their location. Instead of manually searching for weather forecasts, users can interact with the bot and ask for the desired information. The application is designed to be user-friendly and delivers accurate weather forecasts based on user queries. This summary can be used in your documentation to explain the key features and benefits of the application.</p>
        
           <h1 class="text-4xl text-slate-300 mt-5" >Frontend (Vue.js)</h1><hr class="border-t border-gray-500">
           <p class="text-justify">The frontend of the application is built using <a href="https://vueframework.com/" class="underline decoration-sky-300 " target="_blank">Vue.js</a>, a JavaScript framework for building user interface. Vue.js offeres a component based architecture, making it easy to manage and resue UI components. It also provides a reactive and declaritive approach to building UI.</p>
            <br>
            <p class="text-justify">Key feature of Vue.js</p>
            <ul class="list-disc list-inside ml-2">
                <li>Component Based architecture</li>
                <li>Reactive data binding</li>
                <li>Vue Router for client side routing</li>
                <li>Vuex for state management</li>
                <li>Vue CLI for project scaffolding and build configuration</li>
            </ul>
            <h1 class="text-justify mt-5 text-slate-300 text-4xl">Backend (Flask)</h1><hr class="border-t border-gray-500">
            <p class="text-justify">The backend of the application is built using Flask, a lightweight Python web framework. Flask allows for rapid development with its simplicity and flexibility. It provides a solid foundation for building RESTful APIs and handling backend logic.</p><br>
            <p class="text-justify">API used: <a href="https://www.weatherapi.com/" class="underline decoration-sky-300">weatherAPI.com</a> </p>
            <h1 class="text-justify mt-5 text-slate-300 text-4xl">Usage</h1><hr class="border-t border-gray-500">   
            <p class="text-justify mt-2 flex">
                <img src="./images/img1.png" class="rounded" width="400" height="400" alt="img"/>
                <img src="./images/img2.png" class="rounded" width="400" height="400" alt="img"/>
                <img src="./images/img3.png" class="rounded" width="400" height="400" alt="img"/>
            </p>
            <p class="text-justify mt-1">
                Explaing it with the help of the images, one can understand easily. As you can see there are three ways on can give prompt. 
            </p>
        </div>
        <hr class="relative top-40 mx-40">
        <div class="relative top-40 mx-40">
            <p class="text-slate-300">@2023</p>
        </div>
    </main>
</template>