var fs = require('fs');

var data = fs.readFileSync("6.txt", 'utf-8')
    .split(',')
    .map((x) => parseInt(x));


// console.log(data);

function fishReproduction(population) {
    for (let fishIndex = 0; fishIndex < population.length; fishIndex++) {
        let fish = population[fishIndex]

        if (fish == 0) {
            population[fishIndex] = 7
            population.push(9)
        }
        population[fishIndex] = population[fishIndex] - 1;

    }
    return population
}


let v1 = []

for (let day = 0; day < 80; day++) {

    v1 = fishReproduction(data)
    // console.log("Day ", day, ": ", data);
}

console.log(v1.length)

// var i,j, temporary, chunk = 10;
// for (i = 0,j = array.length; i < j; i += chunk) {
//     temporary = array.slice(i, i + chunk);
// do whatever
// }