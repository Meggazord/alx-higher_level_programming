#!/usr/bin/node
// 102-add_me_maybe.js
// Define the function to increment and call another function

function addMeMaybe(number, theFunction) {
  number++;
  theFunction(number);
}

module.exports = {
  addMeMaybe: addMeMaybe
};
