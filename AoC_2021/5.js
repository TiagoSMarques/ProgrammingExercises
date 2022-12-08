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
        }
        // else {
        //     newArray[2].push(inArray[i]) //horizontal
        // }
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
        // fill horizontal
        for (let p = 0; p < posArray[1].length; p++) {
            let yPos = posArray[1][p][1]
            let x1Pos = posArray[1][p][0]
            let x2Pos = posArray[1][p][2]
            const lineH = Array(this.width).fill(0)

            let x = checkStart(x1Pos, x2Pos) //first elem is the minimum

            lineH.fill(1, x[0], x[1] + 1)

            for (let j = 0; j < lineH.length; j++) {
                this.gameB[yPos][j] += lineH[j];
            }
        }
        // fill vertical
        for (let p2 = 0; p2 < posArray[0].length; p2++) {
            let xPos = posArray[0][p2][0]
            let y1Pos = posArray[0][p2][1]
            let y2Pos = posArray[0][p2][3]
            const lineV = Array(this.height).fill(0)

            let y = checkStart(y1Pos, y2Pos) //first elem is the minimum

            lineV.fill(1, y[0], y[1] + 1)
            // console.log(lineV);

            for (let j = 0; j < lineV.length; j++) {
                this.gameB[j][xPos] += lineV[j];
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



const filteredPositions = getLines(positions)
const gameBoard = new Board(boardSize[0] + 1, boardSize[1] + 1)
const filledBoard = gameBoard.fillPositions(filteredPositions)

const allNums = []
filledBoard.map((x) => allNums.push(...x))

const part1 = allNums.filter(x => x >= 2).length
console.timeEnd("a")

console.log(part1);

// const allNums



// console.log(positions);
console.table(filteredPositions);

// console.log(filledBoard);