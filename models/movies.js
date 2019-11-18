// src: ./modules/movies.js
const db = require('../helpers/database');

module.exports = class Movie {
    static getMovies(genres, keywords) {
        const query = (`
        SELECT
            movie.name AS "title",
            genre.name AS "genre",
            movie.year AS "year",
            movie.imdbRating AS "imdbRating",
            movie.rottenTomatoesRating AS "rottenTomatoesRating",
            movie.metaCriticRating AS "metaCriticRating",
            movie.imdbURL AS "imdbURL",
            movie.posterURL AS "posterURL",
            JSON_OBJECTAGG(streamingService.name, movieStreamingServiceSelection.url) AS "availability"
            -- GROUP_CONCAT(JSON_OBJECT(streamingService.name, movieStreamingServiceSelection.url)) AS "streamServiceURL"
            FROM
                movie
            LEFT JOIN movieGenre
                ON
                    movie.ID = movieGenre.movieID
            LEFT JOIN genre
                ON
                    movieGenre.genreID = genre.ID
            LEFT JOIN movieStreamingServiceSelection
                ON
                    movieStreamingServiceSelection.movieID = movie.ID
            LEFT JOIN streamingService
                ON
                    streamingService.ID = movieStreamingServiceSelection.streamingServiceID
            WHERE 
                (genre.name LIKE CONCAT ("%", ?, "%") OR genre.name IS NULL)
            AND
                (movie.name LIKE CONCAT ("%", ?, "%"))
            AND
            	(streamingService.name IS NOT NULL)
            AND
            	(movieStreamingServiceSelection.url IS NOT NULL)
            GROUP BY movie.ID, genre.ID, movieStreamingServiceSelection.movieID
            
        `);
        const params = [genres, keywords];
        return db.execute(query, params);
    }
}