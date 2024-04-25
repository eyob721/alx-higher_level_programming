#!/usr/bin/node
const argv = require('node:process').argv.slice(2);
const fs = require('fs');

const fileA = fs.readFileSync(argv[0], 'utf-8');
const fileB = fs.readFileSync(argv[1], 'utf-8');
fs.writeFileSync(argv[2], fileA + fileB);
