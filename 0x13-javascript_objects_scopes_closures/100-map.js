#!/usr/bin/node

const list = require('./100-data').list;
const newList = list.map((each, idx) => each * idx);
console.log(list);
console.log(newList);
