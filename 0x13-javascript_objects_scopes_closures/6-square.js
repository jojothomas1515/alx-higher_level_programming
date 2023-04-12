#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      console.log(`${c === undefined ? 'X' : c}`.repeat(this.width));
    }
  }
}

module.exports = Square;
