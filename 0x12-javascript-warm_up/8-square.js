#!/usr/bin/node
let output = '';
const value = parseInt(process.argv[2]);
if (process.argv[2] && !isNaN(value) && value >= 0) {
  for (let i = 0; i < value; i++) {
    for (let j = 0; j < value; j++) output += 'X';
    if (i !== value - 1) output += '\n';
  } console.log(output);
} else console.log('Missing size');
