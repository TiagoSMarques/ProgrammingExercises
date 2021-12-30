var fs = require('fs');


var data = fs.readFileSync("6.txt", 'utf-8')
    .split(',')
    .map((x) => parseInt(x));

console.time("a")

var pop = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
}

data.map((x) => pop[x] += 1)

// console.table(pop);
let nextKey, breedCount = 0

for (let day = 1; day <= 256; day++) {

    // Check for new Fish
    if (pop[0] > 0) {
        breedCount = pop[0]
    }

    //Decrease day by shifting the values 1 key to the left
    for (key in Object.entries(pop).slice(0, -1)) {
        nextKey = String(parseInt(key) + 1)
        pop[key] = pop[nextKey]

    }
    //add the new fish
    pop[8] = 0
    if (breedCount != 0) {
        pop[6] += breedCount
        pop[8] += breedCount
        breedCount = 0
    }
}

//count the total fish
let t = 0
for (key in pop) t += pop[key];

console.timeEnd("a")

console.log(t);