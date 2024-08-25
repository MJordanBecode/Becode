import mongoose from "mongoose";
import Anime from "./../models/animeModel.js"



const getAnime = async (req, res) =>{

    try {
        const anime = await Anime.find();
        return res.status(200).json({ anime });
    } catch(err){
        res.status(500).json({ message: `SERVER ERROR : ${err.message}` });
    }
}


export {
    getAnime
}