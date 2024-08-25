const express = require('express');
const router = express.Router();
const {getUsers, postUser} = require('../controller/userController');

router.get("/", getUsers);


router.post("/", postUser);


module.exports = router; 