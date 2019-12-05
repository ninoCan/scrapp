**I DISCONTINUED THE NODEJS CODE. PROJECT NOW USES PYTHON INSTEAD. SOURCE IS FOUND IN THE `PyScrApp` FOLDER**
# Webscraper scrApp

I am going to follow these tutorials:
 - [An Introduction to Web Scraping with Node
   JS](https://codeburst.io/an-introduction-to-web-scraping-with-node-js-1045b55c63f7
   )
- [Scraping the Web With Node.js](https://scotch.io/tutorials/scraping-the-web-with-node-js )

 - Youtube: [Intro to web scraping with nodejs and
   cheerio](https://www.youtube.com/watch?v=LoziivfAAjE )
 - vimeo: [How to Scrape Web Pages with Node.js and
   Cheerio](https://vimeo.com/31950192 )
 
The first uses [Expressjs](https://expressjs.com/ ), [Request](https://github.com/mikeal/request
), [Cheerio](https://github.com/MatthewMueller/cheerio ) and [Request-promise](https://github.com/request/request-promise ). The second
one does it without request-promise, and it is a bit more verbose and
specific to scraping material from IMDB

## Initialization

While being `ssdb/app` I run

    $ npm install --save request cheerio 
to add the dependencies to our project.
Then I create a folder `/scrApp` and touch `scrapp.js`.

## Inside scrapp.js

Most of the comment are written in the file, refer to the `scrapp.js`.
To keep the file neater, I will add verbose comments here:

1. The "$" is a standard name for the [HTML
DOM](https://www.w3schools.com/js/js_htmldom.asp ) variables. Read more
at [What is the meaning of “$” sign in JavaScript](https://stackoverflow.com/questions/1150381/what-is-the-meaning-of-sign-in-javascript#1150402 )

**I DISCONTINUED THE NODEJS CODE. PROJECT NOW USES PYTHON INSTEAD. SOURCE IS FOUND IN THE `PyScrApp` FOLDER**
