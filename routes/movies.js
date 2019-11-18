// src: ./routes/movies.js

const express = require('express');

const moviesController = require('../controllers/movies.js');

const router = express.Router();

// routes for movies
router.get('/', moviesController.getMovies);

module.exports = router;