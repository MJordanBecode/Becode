const mongoose = require('mongoose');
const dotenv = require('dotenv');

dotenv.config();

async function conntectDb(){

    try{
        mongoose.connect(process.env.MONGODB_CONNECT);
        console.log("connexion successfull");
    }
    catch(err){
        console.log(err);
    }
}
module.exports = conntectDb;