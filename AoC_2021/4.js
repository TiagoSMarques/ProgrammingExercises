const {
    readFileSync
} = require("fs");

console.time("a")

const inputData = readFileSync("4.txt", 'utf-8').split('\n\n');

let numbers = inputData[0].split(",").map(x => parseInt(x));
let boards = []
let positions = []
var BreakException = {};

//parse input into array of boards and sum all numbers of each one
for (let i = 1; i < inputData.length; i++) {
    boards[i - 1] = inputData[i].split("\n");
    let aVals = []

    for (let row = 0; row < boards[i - 1].length; row++) {
        boards[i - 1][row] = (boards[i - 1][row].split(" ")).filter(entry => entry.trim() != '').map((x) => parseInt(x));
        positions[i - 1] = {
            countRow: [0, 0, 0, 0, 0],
            countCol: [0, 0, 0, 0, 0],
            ArrayOfValues: aVals,
            TotalSum: 0,
            numbersSum: 0,
        }
        //build array with board numbers
        boards[i - 1][row].map((x) => aVals.push(x));
    }
    positions[i - 1].TotalSum = aVals.reduce((pv, cv) => pv + cv, 0)
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


let answer = [];
let boardsWin = []


// fills each board with the given numbers and marks the in the "positions"
function fillBoard(numberGuess, boards) {

    let indexes = []
    let isLast = 0
    for (let b = 0; b < boards.length; b++) {
        indexes = findNumIndex(boards[b], numberGuess);
        if (indexes != undefined) {

            positions[b].countRow[indexes[0]] += 1;
            positions[b].countCol[indexes[1]] += 1;
            //check if the board contains the guessed number
            if (positions[b].ArrayOfValues.includes(numberGuess)) {
                positions[b].numbersSum += numberGuess
            }
            //check if the board won
            if (positions[b].countRow[indexes[0]] == 5 || positions[b].countCol[indexes[1]] == 5) {
                // console.log("Board ", b, " wins!!")
                answer.push((positions[b].TotalSum - positions[b].numbersSum) * numberGuess);
                // add Board to win counter
                if (!boardsWin.includes(b)){boardsWin.push(b)}
                //all boards have won
                if (boardsWin.length == boards.length) {
                    throw BreakException
                }
            }

        }
    }
}

try {
    numbers.forEach(function (numberGuess) {
        fillBoard(numberGuess, boards)
    });

} catch (e) {
    if (e !== BreakException) throw e;

}

console.timeEnd("a")

console.log(answer[0]);
console.log(answer.pop());

