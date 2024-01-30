#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <number>');
  process.exit(1);
}

const num = process.argv[2];

// display status code of request
request.get(`https://swapi-api.alx-tools.com/api/films/${num}`, (err, res, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
