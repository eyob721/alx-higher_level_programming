#!/usr/bin/node
const argv = process.argv.slice(2);
const num1 = parseInt(argv[0]);
const num2 = parseInt(argv[1]);

function add (a, b) {
  return a + b;
}

console.log(add(num1, num2));
