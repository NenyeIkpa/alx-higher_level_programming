#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./0-readme.js <file-path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

// read file content in utf-8
fs.writeFile(filePath, content, err => {
  if (err) {
    console.error(err);
  }
});
