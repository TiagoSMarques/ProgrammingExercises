
var MedianFinder = function () {
    this.lista = [];
};

/** 
 * @param {number} num
 * @return {void}
 */
MedianFinder.prototype.addNum = function (num) {
    //arr.splice(index, 0, item); will insert item into arr at the specified index (deleting 0 items first, that is, it's just an insert).
    if (this.lista.length == 0) {
        this.lista.push(num)
    } else {

        for (let index = 0; index < this.lista.length; index++) {
            if (num > this.lista[index]) {
                console.log("aaa");
                this.lista.splice(index, 0, num)
                break;
            }
        }

    }
    console.log(this.lista);
};

/**
 * @return {number}
 */

MedianFinder.prototype.findMedian = function () {
    numEl = this.lista.length
    if (numEl < 1) {
        return null
    }
    else {
        var middle = Math.ceil(numEl / 2 - 1)
        if (numEl % 2 == 0) {
            return (this.lista[middle] + this.lista[middle + 1]) / 2
        } else {
            return this.lista[middle]
        }
    }
};

var obj = new MedianFinder()
obj.addNum(-1)
obj.addNum(-2)
console.log(obj.findMedian());
obj.addNum(-3);
console.log(obj.findMedian());



// var param_2 = obj.findMedian()

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */