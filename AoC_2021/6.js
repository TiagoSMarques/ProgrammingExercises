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


// var fibonacci = (function () {
//     var memo = {};

//     function f(n) {
//         var value;

//         if (n in memo) {
//             value = memo[n];
//         } else {
//             if (n === 0 || n === 1)
//                 value = n;
//             else
//                 value = f(n - 1) + f(n - 2);

//             memo[n] = value;
//         }

//         return value;
//     }

//     return f;
// })();




var i, j, temporary, chunk = 1;
let total = 0
let v1 = []

for (i = 0, j = data.length; i < j; i += chunk) {
    temporary = data.slice(i, i + chunk);

    v1 = []
    for (let day = 0; day < 80; day++) {

        v1 = fishReproduction(temporary)
        // console.log("Day ", day, ":  ", v1, "- pop: ", v1.length);
        if ((day % 6) == 1) {
            console.log("Day ", day, "- pop: ", v1.length);


            console.log(v1.length)
        }
    }
    total += v1.length
}

console.log(total)

// var i,j, temporary, chunk = 10;
// for (i = 0,j = array.length; i < j; i += chunk) {
//     temporary = array.slice(i, i + chunk);
// do whatever
// }