#!/usr/bin/node
const value = parseInt(process.argv[2]);
if (process.argv[2] && !isNaN(value) && value >= 0) {
  for (let i = 0; i < process.argv[2]; i++) console.log('C is fun');
} else console.log('Missing number of occurences');
