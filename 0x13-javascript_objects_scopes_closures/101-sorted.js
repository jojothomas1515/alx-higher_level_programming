#!/usr/bin/node

const dict = require('./101-data').dict;
const result = {};
// for (let x in dict) {
//   if (li[`${dict[x]}`] === undefined) {
//     li[`${dict[x]}`] = [];
//     li[`${dict[x]}`].push(x);
//   } else {
//     li[`${dict[x]}`].push(x);
//   }
// }

const res = Object.entries(dict);
res.forEach(([x, y]) => {
  if (result[y] === undefined) {
    result[y] = [x];
  } else {
    result[y].push(x);
  }
});

console.log(result);
