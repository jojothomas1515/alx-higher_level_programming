#!/usr/bin/node

const proc = require('process');
const val = parseInt(proc.argv[2]);

if (val.toString() === 'NaN') {
  console.log('Not a number');
} else {
  console.log(`My number: ${val}`);
}
