const {
    readFileSync
} = require("fs");

console.time("a")


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
            let xMin = 0
            let xMax = 0

            if (x1Pos < x2Pos) {
                xMin = x1Pos
                xMax = x2Pos
            } else {
                xMin = x2Pos
                xMax = x1Pos
            }
            lineH.fill(1, xMin, xMax + 1)

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

            let yMin = 0
            let yMax = 0

            if (y1Pos < y2Pos) {
                yMin = y1Pos
                yMax = y2Pos
            } else {
                yMin = y2Pos
                yMax = y1Pos
            }
            lineV.fill(1, yMin, yMax + 1)
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

function getVertAndHoriz(inArray) {
    const newArray = [
        [],
        []
    ]

    for (let i = 0; i < inArray.length; i++) {

        let x1 = inArray[i][0]
        let y1 = inArray[i][1]
        let x2 = inArray[i][2]
        let y2 = inArray[i][3]

        //check if the line is vert or hor and store it accordingly
        if (x1 == x2) {
            newArray[0].push(inArray[i]) //vertical
        } else if (y1 == y2) {
            newArray[1].push(inArray[i]) //horizontal
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

const filteredPositions = getVertAndHoriz(positions)
const gameBoard = new Board(boardSize[0] + 1, boardSize[1] + 1)
const filledBoard = gameBoard.fillPositions(filteredPositions)

const allNums = []
filledBoard.map((x) => allNums.push(...x))

const part1 = allNums.filter(x => x >= 2).length
console.timeEnd("a")

console.log(part1);

// const allNums



// console.log(positions);
// console.log(filteredPositions);

// console.log(filledBoard);