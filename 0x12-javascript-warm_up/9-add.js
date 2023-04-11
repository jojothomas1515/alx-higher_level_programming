#!/usr/bin/node

const proc = require('process');
const args = proc.argv;
const a = parseInt(args[2]);
const b = parseInt(args[3]);

function add (a, b) {
  console.log(a + b);
}

add(a, b);
