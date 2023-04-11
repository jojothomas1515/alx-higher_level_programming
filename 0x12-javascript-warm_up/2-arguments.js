#!/usr/bin/node

const proc = require('process');
const argc = proc.argv.length - 2;

if (argc === 0) {
  console.log('No argument');
} else if (argc === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
