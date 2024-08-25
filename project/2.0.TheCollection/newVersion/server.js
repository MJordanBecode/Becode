import express from "express";
import dbConnect from "./backEnd/db/dbconnect.js"
import cors from "cors";
import animeRoute from "./backEnd/routes/animeRoutes.js"

dbConnect();

const app = express();
const port = 3004;


//app.use("/api/users", userRoutes);
app.use("/api/animes", animeRoute )

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});