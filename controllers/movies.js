// src: ./controllers/movies.js
const Movies = require('../models/movies');

// Get movies
exports.getMovies = function (req, res, next) {
    // get params from URL and if they were not set then assign them to be as empty string
    const genres = req.query.genres ? req.query.genres : "";
    const keywords = req.query.search ? req.query.search : "";
    
    // debug / test
    //keywords = keywords.split(" ").join("|");
    console.log(keywords);

    // get movies from database with given search params 
    const movies = Movies.getMovies(genres, keywords)
        // send status to 200 and output result as json
        .then(function result( [movies, fieldData] ){ res.status(200).json({movies}); })
        // if there were an error catch it and throw msg
        .catch(function err (e) { 
            if (!err.statusCode) {
                const error = new Error("An error occurred, please try again later.");
                err.statusCode = 500;
                throw error;
            }
        }
    );   
}