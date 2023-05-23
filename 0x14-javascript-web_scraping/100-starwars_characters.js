#!/usr/bin/node

// using request to get the number of episode Wedge Antilles  appeared
const request = require('request');
const process = require('process');
const argv = process.argv;
const argLen = argv.length;

if (argLen !== 3) { process.exit(-1); }

const uri = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

// check the characters array in each episode json object and checks if the char link is included
function logCharactersName (charLink) {
  request(charLink, (err, res, body) => {
    if (err) {
      console.log(err);
      process.exit(-1);
    } else {
      if (res.statusCode === 200) {
        const char = JSON.parse(body);
        console.log(char.name);
      }
    }
  });
}

// log out the number of episodes the character appeared
function movie (err, response, body) {
  if (err) { console.log(err); } else if (response.statusCode === 200) {
    try {
      const data = JSON.parse(body);
      data.characters.forEach(logCharactersName);
    } catch (excp) {
      process.exit();
    }
  }
}

request(uri, movie);
