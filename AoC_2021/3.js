const {
    readFileSync
} = require("fs");

console.time("a")

var gama = "";
var epsilon = "";
let col = ""

const inputData = readFileSync("3.txt", 'utf-8').split('\n');

for (let i = 0; i < inputData[0].length; i++) {

    col = ""
    inputData.forEach(function (value, index) {
        getEachValFromCol(value, index, i)
    })

    if (col.match(new RegExp("1", "g") || []).length > (col.length) / 2) {
        gama += "1"
        epsilon += "0"
    } else {
        gama += "0"
        epsilon += "1"
    }
}

function getEachValFromCol(value, index, i) {
    col += (value.charAt(i))
}


// part 1 
console.log(parseInt(gama, 2) * parseInt(epsilon, 2));


//part 2

let count1 = 0
let indexArr0 = []
let indexArr1 = []

let oxigen = inputData
let co2 = inputData
col = ""

for (let i = 0; i < inputData[0].length; i++) {

    col = ""
    indexArr1 = []
    indexArr0 = []

    oxigen.forEach(function (value, index) {
        getEachValFromCol2(value, index, i)
    })
    if (col.length != 1) {

        count1 = col.match(new RegExp("1", "g") || []).length
        if (count1 > (col.length) / 2) {
            oxigen = indexArr1.map(ind => oxigen[ind])
        } else if (count1 == (col.length) / 2) {
            oxigen = indexArr1.map(ind => oxigen[ind])
        } else {
            oxigen = indexArr0.map(ind => oxigen[ind])
        }

    }
    col = ""
    indexArr1 = []
    indexArr0 = []

    co2.forEach(function (value, index) {
        getEachValFromCol2(value, index, i)
    })
    if (col.length != 1) {

        count1 = col.match(new RegExp("1", "g") || []).length
        if (count1 > (col.length) / 2) {
            co2 = indexArr0.map(ind => co2[ind])

        } else if (count1 == (col.length) / 2) {
            co2 = indexArr0.map(ind => co2[ind])
        } else {
            co2 = indexArr1.map(ind => co2[ind])
        }
    }
}

function getEachValFromCol2(value, index, i) {
    col += (value.charAt(i))

    if (value.charAt(i) == "1") {
        indexArr1.push(index)
    } else {
        indexArr0.push(index)
    }
}

console.log(parseInt(oxigen, 2) * parseInt(co2, 2));
console.timeEnd("a")