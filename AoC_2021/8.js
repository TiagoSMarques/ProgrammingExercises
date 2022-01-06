var fs = require('fs');

console.time("a")

//parsing the data
const data = fs.readFileSync("8.txt", "utf-8")
    .split('\n');

let logEntry = [];

data.forEach(element => {
    logEntry.push(element.split(' '))
});

//-----------
let part1 = 0
const uniqueNums = [2, 3, 4, 7]


for (let i = 0; i < logEntry.length; i++) {
    let lastDigits = logEntry[i].slice(11, 15)
    // console.log(lastDigits);

    for (let el = 0; el < lastDigits.length; el++) {
        if (uniqueNums.includes(lastDigits[el].length)) {
            part1 += 1
        }
    }
}


console.timeEnd("a")

console.log("part 1: ", part1);