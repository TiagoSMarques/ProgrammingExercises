const fs = require('fs')

console.time("time")

var data = fs.readFileSync("3.txt", 'utf-8')
    .split('\r\n')

let matches = []

for (let i = 0; i < data.length; i++) {
    const sack = data[i];
    let comp1 = [...sack.slice(0, sack.length / 2)];
    let comp2 = [...sack.slice(sack.length / 2)];

    for (let l = 0; l < comp1.length; l++) {
        let item1 = comp1[l]
        if (comp2.some(y => y == item1)) {
            let prior = item1.charCodeAt(0)
            if (prior <= 90) {
                matches.push(prior - 38)
            } else {
                matches.push(prior - 96)
            }
            break;
        }
    }
}

let ans1 = matches.reduce((a, i) => a + i)

console.timeEnd("time")
console.log(ans1);


