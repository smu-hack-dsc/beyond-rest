const HOST = "http://localhost:3000";

const socket = io(HOST);

let messages = [];

socket.on("connect", (data) => {
  console.log("connected to web socket");
  console.log(data);
});

socket.on("disconnect", (data) => {
  console.log("disconnected from web socket");
  console.log(data);
});

socket.on("receiveMessage", (data) => {
  let { name, message } = JSON.parse(data);
  let yourName = document.getElementById("chat-name").value;
  if (yourName !== name) {
    insertIncomingMessage(name, message);
    document
      .getElementById("last-pointer")
      .scrollIntoView({ behavior: "smooth" });
  }
});

function sendMessage() {
  //checks if you have a name
  let yourName = document.getElementById("chat-name").value;

  if (yourName) {
    //get message from input box
    let chatInput = document.getElementById("chat-input");
    let message = chatInput.value;

    //only sends message if there is one
    if (message) {
      let messageObject = {
        name: yourName,
        message: message,
      };

      //converts your message object to a string for socketio emitting
      let messageObjectString = JSON.stringify(messageObject);

      //adds your sent message to the message history
      messages.push(messageObject);

      socket.emit("chatMessage", messageObjectString);

      // inserts chat bubble into the chat container
      insertOwnMessage(message);
      //clears chat input box
      chatInput.value = "";

      // scrolls to latest message
      document
        .getElementById("last-pointer")
        .scrollIntoView({ behavior: "smooth" });
    } else {
      //creates an alert to remind you to type a message
      alert("Please type in your message!");
    }
  } else {
    //creates an alert to remind you to give yourself a name
    alert("Please type in your name!");
  }
}

function insertOwnMessage(message) {
  let messageHtml = `<div class="chat chat-end">
<div class="chat-bubble chat-bubble-primary">${message}</div>
</div>`;
  document
    .getElementById("last-pointer")
    .insertAdjacentHTML("beforebegin", messageHtml);
}

function insertIncomingMessage(name, message) {
  let messageHtml = `<div class="chat chat-start">
  <div class="chat-header">
  ${name}
<div class="chat-bubble chat-bubble-secondary">${message}</div>
</div>
</div>`;
  document
    .getElementById("last-pointer")
    .insertAdjacentHTML("beforebegin", messageHtml);
}
