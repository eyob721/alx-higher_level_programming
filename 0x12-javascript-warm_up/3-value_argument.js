#!/usr/bin/node
/* NOTE: To get the actual arguments to the script start from the 2nd index */
const argv = require('node:process').argv.slice(2);
if (argv[0] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[0]);
}
