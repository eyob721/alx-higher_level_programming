#!/usr/bin/node
/* NOTE: To get the actual arguments to the script start from the 2nd index */
const argv = require('node:process').argv.slice(2);

if (argv.length === 0) {
  console.log('No argument');
} else if (argv.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
