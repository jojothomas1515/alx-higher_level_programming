#!/usr/bin/node

// using request to the title of the star wars episode passed as id
const request = require('request');
const process = require('process');
const argv = process.argv;
const argLen = argv.length;

if (argLen !== 3) { process.exit(-1); }

const uri = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

function statusCode (err, response, body) {
  if (err) { console.log(err); } else if (response.statusCode === 200) { console.log(JSON.parse(body).title); }
}

request(uri, statusCode);
