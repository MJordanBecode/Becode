const User = require('../model/userModel');

async function getUsers(req, res){
    try{
        const users = await User.find();
        res.json(users);
    }
    catch(err){
        console.log(err);
    };
};

async function postUser(req, res){
    try{
        const {name, email} = req.body;
        const user = new User({name , email});
        await user.save();
    }
    catch(err){
        console.log(err);
    }
}

module.exports = {getUsers, postUser};
