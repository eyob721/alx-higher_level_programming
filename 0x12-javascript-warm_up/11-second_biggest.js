#!/usr/bin/node
const argv = process.argv.slice(2);

function toNumberArray (arr) {
  const numArray = [];
  for (const i in arr) numArray.push(Number(arr[i]));
  return numArray;
}

if (argv.length <= 2) console.log(0);
else {
  console.log(
    toNumberArray(argv).sort(function (a, b) {
      return b - a;
    })[1]
  );
}
