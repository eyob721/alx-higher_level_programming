#!/usr/bin/node
/* NOTE: To get the actual arguments to the script start from the 2nd index */
const argv = require('node:process').argv.slice(2);
const num = parseInt(argv[0]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
