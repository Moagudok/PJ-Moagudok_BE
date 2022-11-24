const { Server } = require("socket.io");
const { ObjectId } = require("mongodb");
const { MongoClient, ServerApiVersion } = require("mongodb");
const express = require("express");
const http = require("http");
const app = express();
const port = process.env.PORT || 8008;
const server = http.createServer(app);
const io = new Server(server);
const bodyParser = require("body-parser").json();
const users = [];
const mongoDBuri = require("./secure.json");
const uri = mongoDBuri['mongodbURI']
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverApi: { version: ServerApiVersion.v1 },
});
client.connect((err) => {
  const chatDB = client.db("moa_gudok").collection("chat");
});

const chatDB = client.db("moa_gudok").collection("chat");

const chatSave = async (data) => {
  await chatDB.insertOne(data);
}

app.get("/", (req, res) => {
  res.status(200).json({ msg: "Server Moa Gudok Chat Server" });
});

app.get("/chatList", (req, res) => {
  const { room } = req.query;
  chatDB.find({ room }).sort({ _id: -1 }).limit(20).toArray((err, result) => {
    if (err) throw err;
    result.reverse();
    res.status(200).json(result);
  });
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
  socket.on("chat message", (room, user, userName, message) => {
    socket.in(room).emit("chat message", room, user, message, users);
    console.log(message);
    const chatDoc = { user, message, room, userName, time: new Date() };
    chatSave(chatDoc);
  });
});

server.listen(port, () => {
  console.log(`서버시작 포트${port}`);
});
