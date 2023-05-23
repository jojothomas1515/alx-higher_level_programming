#!/usr/bin/node

// reading files with fs
const fs = require('fs');
const process = require('process');
const argv = process.argv;
const argLen = argv.length;

if (argLen !== 3) { process.exit(-1); }

const path = argv[2];

fs.readFile(path, 'utf-8', (err, data) => {
  if (err) { console.log(err); } else {
    console.log(data);
  }
});
