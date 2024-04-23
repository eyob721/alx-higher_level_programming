#!/usr/bin/node
/**
 * NOTE: To get the actual arguments to the script start from the 2nd index.
 * INFO: You can also use the process object without requiring it in NodeJs.
 */
const argv = process.argv.slice(2);
const num = parseInt(argv[0]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
  process.exit();
}
for (let i = 0; i < num; ++i) {
  console.log('C is fun');
}
