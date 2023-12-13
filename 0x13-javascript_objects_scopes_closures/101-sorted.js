#!/usr/bin/node

const dict = require('./101-data').dict;

function occurencesInDict (dict) {
  const occurenceDict = {};
  for (const userId in dict) {
    const occurences = dict[userId];
    if (occurences in occurenceDict) {
      occurenceDict[occurences].push(parseInt(userId));
    } else { occurenceDict[occurences] = [parseInt(userId)]; }
  }
  return occurenceDict;
}

const newDict = occurencesInDict(dict);
console.log(newDict);
