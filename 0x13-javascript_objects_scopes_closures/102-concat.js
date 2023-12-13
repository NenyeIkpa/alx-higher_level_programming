#!/usr/bin/node

const args = require('process').argv;
const fs = require('fs');
const contentFile1 = fs.readFileSync(args[2], 'utf8');
const contentFile2 = fs.readFileSync(args[3], 'utf8');
const concatenated = contentFile1 + contentFile2;
fs.writeFileSync(args[4], concatenated, 'utf8');
