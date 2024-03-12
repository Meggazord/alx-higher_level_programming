#!/usr/bin/node
// 7-multi_c.js
// a script that prints x times “C is fun”

const arg = process.argv[2];

const number = parseInt(arg);

if (!isNaN(number)) {
  console.log("Missing number of occurrences");
} else {
  for (let i = 0; i < number; i++)
    console.log("C is fun");
}
