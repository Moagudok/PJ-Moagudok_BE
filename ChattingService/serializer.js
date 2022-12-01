import mongoose from "mongoose";
import { security } from "./secure.js";
//secure.json File import
mongoose.connect(security.mongodbURI, {
  // useNewUrlPaser: true,
  // useUnifiedTofology: true,
  // useCreateIndex: true,
  // useFindAndModify: false,
  dbName: "moa_gudok",
}
)
  .then(() => console.log('***** MongoDB conected *****'))
  .catch((err) => {
    console.log(err);
  });

// 스키마 생성
const Schema = mongoose.Schema;
const chatMessage = new Schema({
  user: String,
  room: String,
  userName: String,
  message: String,
  time: Date,
});
const roomList = new Schema({
  sellerId: Number,
  room: String,
});

// 모델 생성
export const Chat = mongoose.model('Chat', chatMessage);
export const Room = mongoose.model('Room', roomList);

// 데이터 생성
export const chatSave = (chatDoc) => {
  const chatmsg = new Chat(chatDoc);
  chatmsg.save((err, result) => {
    if (err) throw err;
  });
}

export const roomSave = (roomDoc) => {
  const room = new Room(roomDoc);
  room.save((err, result) => {
    if (err) throw err;
  });
}

export const findRoom = async (room) => {
  return await Room
    .find({
      room: room,
    })
    .exec();
}