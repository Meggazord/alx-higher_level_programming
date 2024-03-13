#!/usr/bin/node
// 101-call_me_moby.js
// Define the function to execute x times

function callMeMoby(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = {
  callMeMoby: callMeMoby
};
