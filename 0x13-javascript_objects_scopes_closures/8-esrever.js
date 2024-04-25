#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  let item = null;

  while (list.length) {
    item = list.pop();
    reversedList.push(item);
  }
  return reversedList;
};
