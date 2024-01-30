#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <url>');
  process.exit(1);
}

const url = process.argv[2];

// display status code of request
request.get(`${url}`, (err, res, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  }
  let count = 0;
  const WEDGE_ANTILLES_ID = '18';
  const data = JSON.parse(body);
  const films = data.results;
  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;
    for (let j = 0; j < characters.length; j++) {
      const charId = characters[j].split('/')[5];
      if (charId === WEDGE_ANTILLES_ID) {
        count++;
      }
    }
  }
  console.log(count);
});
