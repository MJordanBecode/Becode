import express from "express";
const router = express.Router();
import {
    getAnime
} from "../controllers/animeController.js";


// GET ROUTES

router.get("/", getAnime);


//POST ROUTES
// router.post("/",getAnime );

//DELETE ROUTES
// router.delete("/:identifier", getAnime);

//Update ROUTES
// router.patch("/:id",getAnime);
export default router;