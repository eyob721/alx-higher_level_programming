#!/usr/bin/node
const argv = process.argv.slice(2);
const num = parseInt(argv[0]);

if (isNaN(num)) {
  console.log(1);
  process.exit();
}

function factorial (n) {
  if (n === 0) {
    return 1;
  }
  return (n * factorial(n - 1));
}
console.log(factorial(num));
