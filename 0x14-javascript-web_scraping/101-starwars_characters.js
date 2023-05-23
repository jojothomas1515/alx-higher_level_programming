#!/usr/bin/node

// using request to get the number of episode Wedge Antilles  appeared
const request = require('request');
const process = require('process');
const argv = process.argv;
const argLen = argv.length;

if (argLen !== 3) { process.exit(-1); }

const uri = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

// check the characters array in each episode json object and checks if the char link is included
const logCharactersName = (charLink) =>
  new Promise((resolve, reject) => {
    request(charLink, (err, res, body) => {
      if (err) { reject(err); } else {
        if (res.statusCode === 200) {
          const info = JSON.parse(body);
          resolve(info.name);
        }
      }
    });
  });

// log out the number of episodes the character appeared
function movie (err, response, body) {
  if (err) { console.log(err); } else if (response.statusCode === 200) {
    try {
      const data = JSON.parse(body);
      const results = data.characters.map(logCharactersName);
      Promise.all(results).then(ans => ans.forEach(name => console.log(name)));
    } catch (excp) {
      process.exit();
    }
  }
}

request(uri, movie);
