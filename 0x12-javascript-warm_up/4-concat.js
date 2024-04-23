#!/usr/bin/node
/* NOTE: To get the actual arguments to the script start from the 2nd index */
const argv = require('node:process').argv.slice(2);
console.log(argv[0] + ' is ' + argv[1]);
