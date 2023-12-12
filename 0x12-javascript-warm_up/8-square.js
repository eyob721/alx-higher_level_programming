#!/usr/bin/node
const argv = process.argv.slice(2);
const size = parseInt(argv[0]);
if (isNaN(size)) console.log('Missing size');
else for (let i = 0; i < size; ++i) console.log('X'.repeat(size));
