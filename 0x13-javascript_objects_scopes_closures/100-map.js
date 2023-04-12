#!/usr/bin/node

const list = require('./100-data');

console.log(list.list);
console.log(Array.prototype.map.call(list.list, (val, idx) => val * idx));
