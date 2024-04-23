#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/* DO NOT CHANGE THE CODE ABOVE */
myObject.incr = function () {
  ++myObject.value;
};
/* DO NOT CHANGE THE CODE BELOW */
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
