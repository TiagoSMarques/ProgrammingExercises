const {
    readFileSync
} = require("fs");


const inputData = readFileSync("4.txt", 'utf-8').split('\n\n');

let numbers = inputData[0].split(",").map(x => parseInt(x));
let boards = []
let positions = []
var BreakException = {};

//parse input into array of boards and sum all numbers of each one
for (let i = 1; i < inputData.length; i++) {
    boards[i - 1] = inputData[i].split("\n");
    let Sum = 0
    for (let row = 0; row < boards[i - 1].length; row++) {
        boards[i - 1][row] = (boards[i - 1][row].split(" ")).filter(entry => entry.trim() != '').map((x) => parseInt(x));
        positions[i - 1] = {
            countRow: [0, 0, 0, 0, 0],
            countCol: [0, 0, 0, 0, 0],
            numbersSum: 0,
            TotalSum: Sum
        }
        //sum number in each row
        Sum = positions[i - 1].TotalSum + boards[i - 1][row].reduce((pv, cv) => pv + cv, 0);
        positions[i - 1].TotalSum = Sum
    }
}


// Find the coordenates of the number on the board
function findNumIndex(board, num) {
    let ind = undefined;

    for (let r = 0; r < 5; r++) {
        ind = board[r].findIndex(n => n == num);
        if (ind != -1) {
            return [r, ind]
        }
    }
}


let part1 = [];
// let parte2 = 0

// fills each board with the given numbers and marks the in the "positions"
function fillBoard(numberGuess, boards) {

    let indexes = []
    if (boards.length != 0) {
        for (let b = 0; b < boards.length; b++) {
            indexes = findNumIndex(boards[b], numberGuess);
            if (indexes != undefined) {

                positions[b].countRow[indexes[0]] += 1;
                positions[b].countCol[indexes[1]] += 1;
                positions[b].numbersSum += numberGuess

                if (positions[b].countRow[indexes[0]] == 5 || positions[b].countCol[indexes[1]] == 5) {
                    // console.log("Board ", b, " wins!!")
                    console.log(numberGuess);
                    part1.push((positions[b].TotalSum - positions[b].numbersSum) * numberGuess);
                    boards.splice(b, 1)
                    // console.log(part1);
                    // console.log(boards[b])

                    break;
                }
            }
        }
        console.log(boards);
    } else {
        console.log("Aqui");
        throw BreakException
    }
}

try {
    numbers.forEach(function (numberGuess) {
        fillBoard(numberGuess, boards)
    });

} catch (e) {
    if (e !== BreakException) throw e;

}
console.log(part1);



// console.log(boards);
// console.log(positions);