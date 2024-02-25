const express = require("express");
const http = require("http");
const cors = require('cors');
const { Server } = require("socket.io");

const app = express();

app.use(cors())
const server = http.createServer(app);
const io = new Server(server,{
  cors: {
    origin: "*", // Allow all origins
  }
});

io.on("connection", (socket) => {
  console.log("A user connected");

  // Join a room
  socket.on("joinRoom", (roomId) => {
    socket.join(roomId);
    console.log(`User joined room: ${roomId}`);
  });

  // Handle chat message
  socket.on("chatMessage", (message) => {
    io.emit("receiveMessage", message);
  });

  socket.on("disconnect", () => {
    console.log("User disconnected");
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
