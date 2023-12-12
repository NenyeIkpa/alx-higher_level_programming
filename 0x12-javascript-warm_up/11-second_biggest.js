#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  const points = arr.sort(function (a, b) { return b - a; });
  console.log(points[1]);
}
