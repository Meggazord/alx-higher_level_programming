#!/usr/bin/node
function factorial(n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const arg = process.argv[2];
const num = parseInt(arg);
if (isNaN(num)) {
  console.log(1);
} else {
  console.log(factorial(num));
}
