const path = require("path");
const fs = require("fs");

console.time("a")
let header = []

function isData(row) {
    if (!isNaN(parseInt(row[0]))) {
        return true
    } else {
        header.push(row + "\r\n")
    }
}

function rotZ(value) {
    let tz = value + (90 - value) * 2
    if (tz > 180) {
        tz = tz - 360
    }
    return tz
}

function add180(val) {
    let tx = val + 180
    if (tx > 180) {
        tx = tx - 360
    }
    return tx
}
const file = "CamBRUSELAS_N_RIGHT_B2T_01_path";

const inputData = fs
    .readFileSync(path.join(__dirname, file + ".mdl"), 'utf-8')
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
}

const newfile = file + "_new" + ".mdl"
fs.writeFileSync(newfile, "")
try {
    for (let g = 0; g < header.length; g++) {
        fs.writeFileSync(newfile, header[g], {
            flag: 'a'
        })
        if (g == header.length - 4) {
            for (let rr = 0; rr < positions.length; rr++) {
                let line = ""
                positions[rr].forEach(element => {
                    line += element + ","
                });
                fs.writeFileSync(newfile, line.slice(0, -1) + "\r\n", {
                    flag: 'a'
                })
            }
        }

    }
    //file written successfully
} catch (err) {
    console.error(err)
}