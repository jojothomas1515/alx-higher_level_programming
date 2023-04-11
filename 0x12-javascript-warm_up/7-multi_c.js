#!/usr/bin/node

const proc = require('process');
const arg = parseInt(proc.argv[2]);

if (arg.toString() === 'NaN') {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parseInt(arg); i++) {
    console.log('C is fun');
  }
}
