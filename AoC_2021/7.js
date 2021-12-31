const {
    log
} = require('console');
var fs = require('fs');

console.time("a")

function nthTriangular(n) {
    return (n ** 2 + n) / 2
};

function findMedian(arr) {
    const mid = Math.floor(arr.length / 2),
        nums = [...arr].sort((a, b) => a - b);
    return arr.length % 2 !== 0 ? nums[mid] : (nums[mid - 1] + nums[mid]) / 2;
}
const hPos = fs.readFileSync("7.txt", 'utf-8')
    .split(',')
    .map((x) => parseInt(x));

// evaluate the median to know the smaller distance
let median = findMedian(hPos)

const part1 = hPos.map(x => Math.abs(x - median)).reduce((a, b) => a + b)

let hList = Array(Math.max(...hPos) + 1).fill(0)
let part2 = 100000000

for (let i = 0; i < hList.length; i++) {
    //sums all combined movements of the crab
    hList[i] = hPos.map(x => nthTriangular(Math.abs(x - i))).reduce((a, b) => a + b) //part 2
    if (hList[i] < part2) part2 = hList[i]
}

console.timeEnd("a")

console.log(part1);
console.log(part2);