const HOST = "http://localhost:3000";

const socket = io(HOST);

let messages = [];

// const canvas = document.getElementById("my-canvas");
const jsConfetti = new JSConfetti();

socket.on("connect", (data) => {
  console.log("connected to web socket");
  console.log(data);
});

socket.on("disconnect", (data) => {
  console.log("disconnected from web socket");
  console.log(data);
});

socket.on("receiveMessage", async (data) => {
  await jsConfetti.addConfetti({ emojis: [data] });
  jsConfetti.clearCanvas();
});

function onPress(buttonFeatures) {
  const { value } = buttonFeatures;
  socket.emit("chatMessage", value);
}
