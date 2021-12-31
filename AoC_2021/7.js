var fs = require('fs');

var data = fs.readFileSync("7.txt", 'utf-8')
    .split(',')
    .map((x) => parseInt(x));

console.time("a")

//the not-clever  way to do it 

const hPos = data

function nthTriangular(n) {
    return (n ** 2 + n) / 2
};

let hList = Array(Math.max(...hPos) + 1).fill(0)
let ans = 100000000

for (let i = 0; i < hList.length; i++) {
    //sums all combined movements of the crab
    //hList[i] = hPos.map(x => Math.abs(x - i)).reduce((a, b) => a + b) //part 1
    hList[i] = hPos.map(x => nthTriangular(Math.abs(x - i))).reduce((a, b) => a + b) //part 2
    if (hList[i] < ans) ans = hList[i]
}

console.timeEnd("a")

console.log("Ans: ", ans);