require('dotenv').config();
const mongoose = require('mongoose');

main().catch(err => console.log(err));

async function main(){
    await mongoose.connect(process.env.MONGO_DB_CONNECT);

    const User = mongoose.model('User', {
        name: String,
        age: Number
    });

    const firstPerson = new User({
        name: 'Jordan',
        age: 23
    });

    const secondPerson = new User({
        name: 'Angel',
        age: 23
    });

    console.log(firstPerson, secondPerson);

    await firstPerson.save();
    await secondPerson.save();
}

