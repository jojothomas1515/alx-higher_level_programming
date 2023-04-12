#!/usr/bin/node

function add (a, b) {
  return (a + b);
}

// cooler way to export
module.exports = { add: add };
