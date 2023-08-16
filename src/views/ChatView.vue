<script setup>
  
import axios from "axios";
function sendMessage() {
      const messageInput = document.getElementById("messageInput");
      const chatBox = document.getElementById("chatBox");
      const message = messageInput.value.trim();
      console.log(messageInput.value)
      console.log("chatbox",chatBox,"message",message)
      if (message !== "") {
        var newMessage = document.createElement("div");
        newMessage.className = "user-message";
        newMessage.textContent = message;
        chatBox.appendChild(newMessage);
        messageInput.value = "";
        console.log("in")
        chatBox.scrollTop = chatBox.scrollHeight; // Automatically scroll to the bottom
        console.log(newMessage);
        const payload = {
          'location': message
        }
        console.log(payload)
        axios.get('http://127.0.0.1:5000/w',{params: payload }).then(response => {
            const data = response.data;
            console.log(data)
            const temp = data['temperature']
            const weather = data['weather']['text']
            console
            newMessage = document.createElement('div');
            newMessage.className = "user-message-received";
            newMessage.textContent = 'temparature: '+temp+ "`C "+weather;
            chatBox.appendChild(newMessage)
            console.log("done");}
        ).catch(error => {
            console.log(error);
        })
      }


    }
</script>

<template>
    <main class="home-main relative top-20  bg-slate-100 bg-opacity-5  rounded z-0 mx-40  ">
    <div class="chat-container  bg-slate-100 shadow-inner shadow-slate-300  relative top-20">
      <div class="chat-box" id="chatBox">
        <!-- Chat messages will be displayed here -->
      </div>
      <div class="input-container ">
        <input type="text" class="input-field " id="messageInput" placeholder="Get Weather Forcast here !">
        <button class="send-button" @click="sendMessage()">Send</button>
      </div>
    </div>
  </main>
</template>