const http = require('http');
const express = require('express');
const path = require('path');
const app = express();


app.use(express.json());


app.use(express.static(path.join(__dirname, 'express')));


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'express', 'index.html'));
});


const port = 3000;
const server = http.createServer(app);
server.listen(port, () => {
    console.debug(`Server listening on port ${port}`);
});
