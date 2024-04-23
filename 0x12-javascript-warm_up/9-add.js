#!/usr/bin/node
const argv = process.argv.slice(2);

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

console.log(add(argv[0], argv[1]));
