#!/usr/bin/node

const MySquare = require('./5-square');

class Square extends MySquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
