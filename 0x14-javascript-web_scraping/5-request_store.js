#!/usr/bin/node

// get a page and save it to a file
const process = require('process');
const argv = process.argv;
const argLen = argv.length;
const request = require('request');
const fs = require('fs');

if (argLen !== 4) { process.exit(-1); }

const uri = argv[2];
const path = argv[3];

function saveDataToFile (err, res, body, path) {
  if (err) {
    console.log(err);
    process.exit(-1);
  } else {
    if (res.statusCode === 200) {
      fs.writeFile(path, body, 'utf-8', (errs) => {
        if (err) { console.log(err); }
      });
    }
  }
}

request(uri, (err, res, body) => {
  saveDataToFile(err, res, body, path);
});
