const fs = require('fs')

console.time("time")

let sum = 0;
let sum2 = 0;

let newArray3 = [];

function CheckIfBigger(value, index, array) {
    if (array[index] > array[index - 1]) sum += 1;
}

function Group3(value, index, array) {
    const groupSum = array[index] + array[index + 1] + array[index + 2];
    if (!isNaN(groupSum)) newArray3.push(groupSum);
}

fs.readFile('1.txt', 'utf8', (err, data) => {
    if (err) return console.error(err);

    const numbers = data.split('\n').map((x) => parseInt(x))
    // part 1
    numbers.forEach(CheckIfBigger);
    console.log("Part 1: ", sum);
    // part 2
    sum = 0
    // numbers.forEach(CheckIfBigger3);
    numbers.forEach(Group3);
    newArray3.forEach(CheckIfBigger)
    console.log("Part 2: ", sum2);


    console.timeEnd("time");
})

// function CheckIfBigger3(value, index, array) {
//     let CurrSet = array[index] + array[index + 1] + array[index + 2]
//     let NextSet = array[index + 1] + array[index + 2] + array[index + 3]
//     if (NextSet > CurrSet) sum2 += 1;
// }