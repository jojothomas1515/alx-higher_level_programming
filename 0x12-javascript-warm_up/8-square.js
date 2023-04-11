#!/usr/bin/node

const proc = require('process');
const val = parseInt(proc.argv[2]);

if (val.toString() === 'NaN') {
  console.log('Missing size');
} else {
  for (let i = 0; i < val; i++) {
    console.log('X'.repeat(val));
  }
}
