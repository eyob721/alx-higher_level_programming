#!/usr/bin/node
const argv = process.argv.slice(2);
const num = parseInt(argv[0]);
if (isNaN(num)) {
  console.log('Missing size');
  process.exit();
}
for (let i = 0; i < num; ++i) {
  console.log('X'.repeat(num));
}
