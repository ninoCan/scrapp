// load dependencies
const express = require('express');
const fs = require('fs');
const request = require('request');
const cheerio = require('cheerio');
// define the application
const scrapp = express();

// routes GET request to /scrap
scrapp.get('/scrap', (req,res) => {
    // store the url of the page being scraped into a variable
    url='https://content.viaplay.fi/pcdash-fi/leffat/kaikki?blockId=20822ace006b61ea5811662ab365729e&partial=1&pageNumber=1&sort=recently_added' //viaplay
    url='http://www.imdb.com/title/tt1229340/'; //one imdb entry
    console.log('Currently scraping the url: ' + url);//print the url that we are going to scrape
    // send request to the url and 
    request(url, (error, response, html) => {
        // check if no error has occurred and  a succesfull response was received
        // if (!error && response.statusCode == 200 ) {
        if (!error) {

            // load the html page into the $ variable, see README.md 
            const $ = cheerio.load(html);
            
            const siteBody = $('body')
            console.log(siteBody);
        };        
    });

});

//This should expose the port 8081
scrapp.listen('8081')
console.log('Scraper running');
 
// return the scraped 
module.exports = scrapp;