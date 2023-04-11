#!/usr/bin/node

const proc = require('process')
const val = parseInt(proc.argv);

if (val.toString() === 'NaN') {
  console.log('Missing size');
} else {
  console.log('X'.repeat(val));
}
