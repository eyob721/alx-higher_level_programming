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
  if (a > b) return 1;
  if (a === b) return 0;
  if (a < b) return -1;
}
const argv_sorted = argv.sort(compareNumeric);

console.log(argv_sorted.at(-2));
