#!/usr/bin/node
const argv0 = require('node:process').argv.slice(2)[0];
if (!argv0) console.log('No argument');
else console.log(argv0);
