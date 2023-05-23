#!/usr/bin/node

// with data to file
const fs = require('fs');
const process = require('process');
const argv = process.argv;
const argLen = argv.length;

if (argLen !== 4) { process.exit(-1); }

const path = argv[2];
const data = argv[3];

fs.writeFile(path, data, 'utf-8', (err) => {
  if (err) { console.log(err); }
});
