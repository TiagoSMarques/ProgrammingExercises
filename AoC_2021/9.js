// Find lowest points
var fs = require('fs');

console.time("a")

const data = fs.readFileSync('9.txt')
    .toString()
    .split('\n')
    .map((line) => line.split('').map((x) => parseInt(x)))


let lowPoints = [];

let numRows = data.length
let numColumns = data[0].length

//first number is row second is column

loop1:
for (let row = 0; row < data.length; row++) {

    loop2:
    for (let column = 0; column < data[row].length; column++) {

        let bottomNum = 1 << 100
        let topNum = 1 << 100
        let rightNum = 1 << 100
        let leftNum = 1 << 100

        // console.log("r:", row, " c:", column);
        currNum = data[row][column]
        // console.log(currNum);
        if (row != 0) {
            topNum = data[row - 1][column]
        }
        if (row != numRows - 1) {
            bottomNum = data[row + 1][column]
        }
        if (column != 0) {
            leftNum = data[row][column - 1]
        }
        if (column != numColumns - 1) {
            rightNum = data[row][column + 1]
        }
        // check if there is a smaller number in a cross if there is move onto next number

        if (currNum < topNum &&
            currNum < bottomNum &&
            currNum < leftNum &&
            currNum < rightNum) {
            lowPoints.push(currNum)
        }
    }
}

console.timeEnd("a")
console.log(lowPoints.reduce((a, b) => a + b) + lowPoints.length);
