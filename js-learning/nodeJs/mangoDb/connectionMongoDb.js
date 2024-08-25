const dotenv = require("dotenv");
const mongoose = require("mongoose");

dotenv.config();

export const dbConnect = async () => {
  try {
    mongoose.connect(process.env.MONGO_DB_CONNECT);
    console.log("Connected to MongoDB successfully!");
  } catch (err) {
    console.error(err.message);
    process.exit(1);
  }
};
dbConnect();

module.exports = dbConnect;