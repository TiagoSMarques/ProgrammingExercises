import  sequtils, deques, times
# Simple benchmarking
var t0 = cpuTime()*1000

let data = readFile("6.txt")

var buffer = data[0..2].toDeque
var ans1 = 3

for i in data[3..^1].items:
    buffer.addLast(i)
    inc(ans1)

    if deduplicate(toSeq(buffer)).len == buffer.len:
        # echo i
        break
    
    buffer.popFirst()

echo "Answer 1: ", ans1
echo "CPU time [ms] ", cpuTime()*1000-t0