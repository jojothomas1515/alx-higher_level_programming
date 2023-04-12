#!/usr/bin/node

const proc = require('process');
const fs = require('fs');

const [f1, f2, f3] = proc.argv.slice(2);

if (f1 && f2 && f3) {
  fs.readFile(f1, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
    fs.appendFile(f3, data, () => {});
  });
  fs.readFile(f2, 'utf-8', (err, data) => {
    if (err) {
      console.log(err);
    }
    fs.appendFile(f3, data, () => {});
  });
}
