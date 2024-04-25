#!/usr/bin/node
const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    c = c === undefined ? 'X' : c;
    console.log((c.repeat(this.width) + '\n').repeat(this.height).trimEnd());
  }
}

module.exports = Square;
