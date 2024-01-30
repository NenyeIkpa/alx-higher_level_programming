#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: node script.js <URL> <FilePath>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    process.exit(1);
  }

  if (response && response.statusCode === 200) {
    fs.writeFile(filePath, body, { encoding: 'utf-8' }, (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
