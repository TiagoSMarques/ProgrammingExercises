const fs = require('fs')

console.time("time")
var data = fs.readFileSync("1.txt", 'utf-8')
    // separar as cargas de cada elfo num array
    .split('\n\r\n')
    // converter para inteiro, remover espaços em branco e separar as calorias
    .map(x => (x.split('\r').filter(s => s != '').map(t => parseInt(t))))
    // somar as colorias de cada elfo
    .map(y => y.reduce((p, c) => p + c))
    // ordenar o array do maior para o mais pequeno
    .sort((a, b) => b - a)
    // extrair os 3 maiores
    .slice(0, 3);

// console.log(data);
let ans1 = Math.max(...data)
let ans2 = data.reduce((acc, n) => acc + n)

console.timeEnd("time")
console.log(ans1, ans2);
