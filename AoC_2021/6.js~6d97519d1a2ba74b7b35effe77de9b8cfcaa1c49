var fs = require('fs');


var data = fs.readFileSync("6.txt", 'utf-8')
    .split(',')
    .map((x) => parseInt(x));

console.time("a")


const pop = Array(8).fill(0)

data.map((x) => pop[x] += 1)

let breedCount = 0

for (let day = 1; day <= 256; day++) {

    // Check for new Fish
    if (pop[0] > 0) {
        breedCount = pop[0]
    }

    //Decrease day by shifting the values 1 key to the left
    pop.slice(0, -1).forEach((value, index) => {
        pop[index] = pop[index + 1]
    });

    //add the new fish
    pop[8] = 0
    if (breedCount != 0) {
        pop[6] += breedCount
        pop[8] += breedCount
        breedCount = 0
    }
}

//count the total fish
let ans = pop.reduce((a, b) => a + b)

console.timeEnd("a")
console.log(ans);