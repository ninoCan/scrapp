// src: /app.js

// src: ./app.js
const express = require ('express');
const bodyParser = require('body-parser');

// get routes data
const moviesRoutes = require('./routes/movies.js');

// define app & config defaults
const app = express();
app.use(bodyParser.json());

// set cors
app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
    next();
});

// use routes
app.use('/movies', moviesRoutes);

// Listen port 8888
app.listen(8888);