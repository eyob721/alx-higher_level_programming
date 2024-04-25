#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};

for (const id in dict) {
  const occur = dict[id];

  if (newDict[occur] === undefined) {
    newDict[occur] = [];
  }

  newDict[occur].push(id);
}

console.log(newDict);
