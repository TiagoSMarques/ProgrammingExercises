const fs = require('fs')

console.time("a")

let pos = [0, 0, 0]

function Increment(value) {
    const line = value.split(" ")

    if (line[0] == "forward") {
        pos[0] += parseInt(line[1])
    } else if (line[0] == "down") {
        pos[1] += parseInt(line[1])
    } else {
        pos[1] -= parseInt(line[1])
    }
}

function Increment2(value) {
    const line = value.split(" ")

    if (line[0] == "forward") {
        pos[0] += parseInt(line[1])
        pos[1] += parseInt(line[1]) * parseInt(pos[2])
    } else if (line[0] == "down") {
        pos[2] += parseInt(line[1])
    } else {
        pos[2] -= parseInt(line[1])
    }
}

const data = fs.readFileSync('2.txt', 'utf8')

// part 1
data.split("\n").forEach(Increment)
console.log(pos[0] * pos[1]);

// part 2
pos = [0, 0, 0]
data.split("\n").forEach(Increment2)
console.log(pos[0] * pos[1]);

console.timeEnd("a")