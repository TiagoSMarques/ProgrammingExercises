const num = BigInt(2 ** 1000)
const numArr = String(num).split('')

// console.log(numArr);

// function add(a, b) {
//     return a + b
// }

const add = (preVal, currVal) => parseInt(currVal) + parseInt(preVal);

console.log(numArr.reduce(add));