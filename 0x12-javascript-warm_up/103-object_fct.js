#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/* My code - Start */
myObject.incr = function () {
  ++myObject.value;
};
/* My code - End */
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
