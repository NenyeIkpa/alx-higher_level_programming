#!/usr/bin/node
const { argv } = require('node:process');
let myVar = 'No argument';
if (argv.length <= 2) console.log(myVar);
else if (argv.length === 3) { myVar = 'Argument found'; console.log(myVar); } else { myVar = 'Arguments found'; console.log(myVar); }
