const {
    readFileSync
} = require("fs");

console.time("a")

function checkStart(a, b) {
    let v = [null, null]
    if (a < b) {
        v[0] = a
        v[1] = b
    } else {
        v[0] = b
        v[1] = a
    }
    return v
}

function getLines(inArray) {
    const newArray = [
        [],
        [],
        []
    ]

    //check if the line is vert or hor and store it accordingly + determine size of the board
    for (let i = 0; i < inArray.length; i++) {

        let x1 = inArray[i][0]
        let y1 = inArray[i][1]
        let x2 = inArray[i][2]
        let y2 = inArray[i][3]

        if (x1 == x2) {
            newArray[0].push(inArray[i]) //vertical
        } else if (y1 == y2) {
            newArray[1].push(inArray[i]) //horizontal
        } else {
            newArray[2].push(inArray[i]) //diagonal
        }
        // size of the board
        if (x1 > boardSize[0]) {
            boardSize[0] = x1
        } else if (x2 > boardSize[0]) {
            boardSize[0] = x2
        }
        if (y1 > boardSize[1]) {
            boardSize[1] = y1
        } else if (y2 > boardSize[1]) {
            boardSize[1] = y2
        }
    }
    return newArray
}

class Board {
    constructor(width, height) {
        this.width = width
        this.height = height
        this.gameB = Array(this.height).fill().map(() => Array(this.width).fill(0))

    }
    fillPositions(posArray) {
        for (let orient = 0; orient < posArray.length; orient++) {
            // first loop is the vertial 2nd is horizontal, 3rd is diagonal
            for (let p = 0; p < posArray[orient].length; p++) {
                let x1 = posArray[orient][p][0]
                let y1 = posArray[orient][p][1]
                let x2 = posArray[orient][p][2]
                let y2 = posArray[orient][p][3]

                while (x1 != x2 || y1 != y2) {

                    this.gameB[x1][y1] += 1;

                    (x1 < x2) ? x1++ : ((x1 > x2) && x1--);
                    (y1 < y2) ? y1++ : ((y1 > y2) && y1--);
                }

                this.gameB[x1][y1] += 1;
            }
        }
        return this.gameB
    }
}


const positions = []
const inputData = readFileSync("5.txt", 'utf-8').split('\n');

inputData.forEach(element => {
    positions.push(element
        .replace("->", ",")
        .split(",")
        .map((x) => parseInt(x)))
});

const boardSize = [0, 0]

//part 1
// const filteredPositions = getLines(positions).slice(0, 2)

//part 2
const filteredPositions = getLines(positions)
const gameBoard = new Board(boardSize[1] + 1, boardSize[0] + 1)

const filledBoard = gameBoard.fillPositions(filteredPositions)
// console.table(filledBoard);

const allNums = []
filledBoard.map((x) => allNums.push(...x))

const ans = allNums.filter(x => x >= 2).length
console.timeEnd("a")

console.log(ans);