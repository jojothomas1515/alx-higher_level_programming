#!/usr/bin/node

const proc = require('process');
const val = parseInt(proc.argv[2]);

if (val.toString() === 'NaN' || val === 1) {
  console.log(1);
} else {
  console.log(factorial(val));
}

function factorial (val) {
  if (val === 0) {
    return (1);
  }
  return val * factorial(val - 1);
}
