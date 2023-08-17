<script setup>

import axios from "axios";
function sendMessage() {
    const messageInput = document.getElementById("messageInput"); //gets input element 
    const chatBox = document.getElementById("chatBox");
    const message = messageInput.value.trim(); //gets message from the messageInput

    if (message !== "") {
        //displays the text written in input box
        var newMessage = document.createElement("div");
        newMessage.className = "user-message";
        newMessage.textContent = message;
        chatBox.appendChild(newMessage);

        //resets the input box to empty
        messageInput.value = "";


        chatBox.scrollTop = chatBox.scrollHeight; // Automatically scroll to the bottom


        const payload = {
            'location': message
        }
        axios.get('http://127.0.0.1:5000/w', { params: payload }).then(response => {
            //recived data from the backend
            const data = response.data;

            console.log(data);

            //outter div element 
            newMessage = document.createElement('div');
            newMessage.className = "user-message-received"


            const keysList = Object.keys(data);
            const valuesList = Object.values(data);

            const dict = {};

            for (var j = 0; j < Object.keys(data).length; j++) {
                if (keysList[j] == 'weather') {
                    console.log("ind", valuesList[j]['text'])
                    dict.WEATHER = valuesList[j]['text'];
                    dict.icon = valuesList[j]['icon'];
                }
                else {
                    if (keysList[j] == 'suggestion') {
                        dict[""] = valuesList[j]
                    }
                    else {
                        const val = keysList[j]
                        val.toUpperCase();
                        dict[val] = valuesList[j];
                    }

                }
            }
            console.log("dict", dict)
            for (let key in dict) {
                if (key == 'icon') {
                    const newImg = document.createElement('img');
                    newImg.className = 'weather-img';
                    newImg.src = dict[key]
                    newMessage.appendChild(newImg);
                }
                else {
                    const newPEle = document.createElement('p');
                    newPEle.className = "weather-p"
                    newPEle.textContent = key + " : " + dict[key];
                    newMessage.appendChild(newPEle);
                }

            }

            chatBox.appendChild(newMessage)
            console.log("done");
        }
        ).catch(error => {
            console.log(error);
        })
    }


}
</script>

<template>
    <main class="home-main relative top-20    rounded z-0 mx-40  ">
        <div class="chat-container  bg-slate-100 shadow-inner shadow-slate-300  relative top-20">
            <div class="chat-box" id="chatBox">
                <!-- Chat messages will be displayed here -->
            </div>
            <div class="input-container ">
                <input type="text" class="input-field " id="messageInput" placeholder="Get Weather Forcast here !">
                <button class="send-button" @click="sendMessage()">Send</button>
            </div>
        </div>
        <hr class="relative top-40 mx-40">
        <div class="relative top-40 mx-40">
            <p class="text-slate-300">@2023</p>
        </div>
    </main>
</template>