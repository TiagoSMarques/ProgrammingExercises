const path = require("path");
const fs = require("fs");

console.time("a")

function isData(row) {
    return !isNaN(parseInt(row[0]));
}

function rotZ(value) {
    return value + (90 - value) * 2
}

function add180(val) {
    return val + 180
}

const inputData = fs
    .readFileSync(path.join(__dirname, "CamBRUSELAS_N_RIGHT_B2T_01_path.mdl"), 'utf-8')
    .split("\r\n")
    .filter(isData)

let positions = [];

for (let i = 0; i < inputData.length; i++) {
    positions.push(inputData[i].split(",").map((x) => parseFloat(x)))
}

let a = 0;
let b = 1;
let c = 0;

let currQuadrant = 1
let targetQuadrant = 4

switch (steps) {
    case value:

        break;

    default:
        break;
}

let transfPos = [1 - 2 * a, 1 - 2 * b, 1 - 2 * c]

for (let pos = 0; pos < positions.length; pos++) {
    positions[pos][0] = positions[pos][0] * transfPos[0]
    positions[pos][1] = positions[pos][1] * transfPos[1]
    positions[pos][2] = positions[pos][2] * transfPos[2]

    let rx = positions[pos][3];
    let rz = positions[pos][5];

    if (a == 1 & b == 0 & (c == 0 || c == 1)) {
        positions[pos][5] = rotZ(rz)
    } else if (a == 0 & b == 1 & (c == 0 || c == 1)) {
        positions[pos][3] = add180(rx)
    } else if (a == 1 & b == 1 & (c == 1 || c == 0)) {
        positions[pos][3] = add180(rx)
        positions[pos][5] = rotZ(rz)

    } else {
        console.log("problema");
    }


    console.log(positions);


    // case a == 1 & b == 0 & c == 0:
    //     positions[pos][5] = rotZ(rz)
    //     break;
    // case a == 0 & b == 1 & c == 0:
    //     positions[pos][3] = add180(rx)
    //     break;

    // case a == 1 & b == 1 & c == 0:
    //     positions[pos][5] = rotZ(rz)
    //     break;
    // case a == 0 & b == 1 & c == 1:
    //     positions[pos][3] = add180(rx)
    //     break;
    // case a == 1 & b == 0 & c == 1:
    //     positions[pos][5] = rotZ(rz)
    //     break;
    // case a == 1 & b == 1 & c == 1:
    //     positions[pos][3] = add180(rx)
    //     positions[pos][5] = rotZ(rz)
    //     break;