#!/usr/bin/node
const argv = process.argv.slice(2);
const num = parseInt(argv[0]);

if (isNaN(num)) {
  console.log(1);
  process.exit();
}

let factorial = 1;
for (let i = 1; i <= num; ++i) {
  factorial *= i;
}
console.log(factorial);
