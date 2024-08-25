import mongoose from 'mongoose';
import { Grid } from 'gridfs-stream';

const gfs = Grid(conn.db, mongoose.mongo);

// Pour stocker un fichier
const writeStream = gfs.createWriteStream({
    filename: 'myImage.png',
    content_type: 'image/png'
});
fs.createReadStream('/path/to/image.png').pipe(writeStream);

// Pour récupérer un fichier
gfs.files.findOne({ filename: 'myImage.png' }, (err, file) => {
    if (err || !file) {
        return console.error('File not found');
    }
    const readStream = gfs.createReadStream({ filename: file.filename });
    readStream.pipe(res); // Vous pouvez envoyer le fichier en réponse HTTP
});
