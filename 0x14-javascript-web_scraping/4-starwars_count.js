#!/usr/bin/node

// using request to get the number of episode Wedge Antilles  appeared
const request = require('request');
const process = require('process');
const argv = process.argv;
const argLen = argv.length;

if (argLen !== 3) { process.exit(-1); }

const uri = argv[2];

// check the characters array in each episode json object and checks if the char link is included
function movieFilterOnChar (movie) {
  return movie.characters.filter(link => link.endsWith('18/')).length;
}

// log out the number of episodes the character appeared
function numOfMovies (err, response, body) {
  if (err) { console.log(err); } else if (response.statusCode === 200) {
    try {
      const data = JSON.parse(body);
      const films = data.results.filter(movieFilterOnChar);
      console.log(films.length);
    } catch (excp) {
      process.exit();
    }
  }
}

request(uri, numOfMovies);
