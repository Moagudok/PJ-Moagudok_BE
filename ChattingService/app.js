import { chatSave, roomSave, Chat, Room, findRoom } from './serializer.js';
import { Server } from 'socket.io';
import express from 'express';
import http from 'http';
const app = express();
const port = process.env.PORT || 8008;
const server = http.createServer(app);
const io = new Server(server);
const users = [];

server.listen(port, () => {
  console.log(`서버시작 포트는 ${port}`);
});

app.get("/", async (req, res) => {
  chatSave({
    user: "user",
    room: "room1",
    userName: "user1",
    message: "hello world",
    time: new Date(),
  });
  res.status(200).json({ msg: hello() });
});

app.get("/roomsave", async (req, res) => {
  const room = req.query.room;
  findRoom(room);
  res.status(200).json({ msg: hello() });
});

app.get("/roomlist", async (req, res) => {
  const room = req.query.room;
  const roomList = await Room.find({
    room: room,
  });
  res.status(200).json({ msg: roomList });
});

app.get("/chatlist", (req, res) => {
  const room = req.query.room;
  Chat.find({ room: room }, (err, result) => {
    if (err) throw err;
    res.status(200).json(result);
  }
  );
});

const chat = io.of("/chat");

chat.on("connection", (socket) => {
  socket.on("disconnect", () => {
    console.log("User disconnected");
  });
  socket.on("join", (room, user) => {
    socket.join(room);
    users.push({
      room: room,
      user: user,
    });
    socket.broadcast.emit("join users", users);
    console.log(`${user} has joined the room`);
    console.log(users);
  });
  socket.on("leave", (room, user) => {
    socket.leave(room)
    users.splice(users.findIndex((item) => item.user === user), 1);
    console.log(`User left ${room}`);
    console.log(users);
  });
  socket.on("chat message", async (room, user, userName, message, seller) => {
    socket.in(room).emit("chat message", room, user, message, users);
    const roomList = await findRoom(room);
    if (roomList.length == 0) {
      roomSave({
        sellerId: seller,
        room: room,
      });
    }
    const chatDoc = {
      user: user,
      room: room,
      userName: userName,
      message: message,
      time: new Date(),
    };
    chatSave(chatDoc);
  });
});
