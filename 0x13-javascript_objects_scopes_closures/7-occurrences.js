#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) count++;
  }
  return count;
  // return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
