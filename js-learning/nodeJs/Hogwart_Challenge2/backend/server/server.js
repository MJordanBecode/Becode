// Importation du module Express
const express = require('express');
const connect = require('./dbConnect');
const userRoutes = require('../routes/usersRoute');
connect();

// Création d'une instance de l'application Express
const app = express();
app.use(express.json());


// Définition du port sur lequel le serveur écoutera
const port = 3000;

// Définition d'une route pour l'URL racine ('/')
app.use("/api/users", userRoutes);

// Démarrage du serveur et écoute sur le port défini
app.listen(port, () => {
  console.log(`Le serveur est démarré et écoute sur le port ${port}`);
});
