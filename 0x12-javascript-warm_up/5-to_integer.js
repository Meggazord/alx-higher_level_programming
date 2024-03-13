#!/usr/bin/node
// 5-to_integer.js
// Get the first argument from the command line

const arg = process.argv[2];

const number = parseInt(arg);

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log("Not a number");
}
