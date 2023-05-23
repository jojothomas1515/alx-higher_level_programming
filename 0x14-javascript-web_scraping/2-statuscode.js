#!/usr/bin/node

// using request to get web status code
const request = require('request');
const process = require('process');
const argv = process.argv;
const argLen = argv.length;

if (argLen !== 3) { process.exit(-1); }

const uri = argv[2];

function statusCode (err, response, body) {
  if (err) { console.log(err); } else { console.log(`code: ${response.statusCode}`); }
}

request(uri, statusCode);
