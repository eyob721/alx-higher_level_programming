#!/usr/bin/node
const argv = require('node:process').argv.slice(2);

if (argv.length < 2) {
  console.log(0);
  process.exit();
}

/* NOTE: To sort by thier numeric value use a custom sorting function */
function compareNumeric (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  return b - a;
}
const argvSorted = argv.sort(compareNumeric);
console.log(parseInt(argvSorted[1]));
