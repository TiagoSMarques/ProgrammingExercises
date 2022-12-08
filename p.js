/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
    let profit = 0;
    maxVal = Math.max(...prices)
    minVal = Math.min(...prices)

    if (prices.indexOf(minVal) < prices.lastIndexOf(maxVal)) {
        return maxVal - minVal
    }
    else {
        for (let i = prices.length - 1; i >= 0; i--) {
            const element = prices[i];
            for (let x = i - 1; x >= 0; x--) {
                const sub = prices[i] - prices[x];
                if (sub > profit) {
                    profit = sub
                }
            }
        }
    }
    return profit
};

let prices = [7, 1, 5, 3, 6, 4, 7]

console.log(maxProfit(prices))

