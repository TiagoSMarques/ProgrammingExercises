import  sequtils, deques, times
# Simple benchmarking
var t0 = cpuTime()*1000

let data = readFile("6.txt")

proc ans(data : string, c : int): int =
    
    var buffer = data[0..c-2].toDeque
    var ans = c-1

    for i in data[c-1..^1].items:
        buffer.addLast(i)
        inc(ans)

        if deduplicate(toSeq(buffer)).len == buffer.len: break
        buffer.popFirst()
    ans



echo "Answer 1: ", ans(data,4)
echo "Answer 2: ", ans(data,14)

echo "CPU time [ms] ", cpuTime()*1000-t0