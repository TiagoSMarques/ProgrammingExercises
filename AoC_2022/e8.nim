import  sequtils, times, strutils
# Simple benchmarking
var t0 = cpuTime()*1000

let data = readFile("8.txt").splitLines
var rows,cols : seq[seq[int]]

# build rows
for line in data:
    rows.add(map(toSeq(line.items), proc(x: char): int = parseInt($x)))

# build cols
newSeq(cols,rows[0].len)
for l in rows:
    for idx,n in l: cols[idx].add(n)

proc ans1(rows,cols : seq[seq[int]]): int =    
    var ans =2*cols[0].len-2 + 2*cols.len-2
    var counter = 0;
    for y,l in rows[1..^2]:
        for x,val in l[1..^2]:
            counter=0
            # check left
            if not rows[y+1][0..x].anyIt(it>=val):
                inc(counter)
                # echo "found left " ,   x,y, "  ", val
            # check right
            if not rows[y+1][x+2..^1].anyIt(it>=val):
                inc(counter)
                # echo "found right ",  x,y, "  ", val
            # Check up
            if not cols[x+1][0..y].anyIt(it>=val):
                inc(counter)
                # echo "found up ",   x,y, "  ", val
            # Check down
            if not cols[x+1][y+2..^1].anyIt(it>=val):
                inc(counter)
                # echo "found down ",   x,y, "  ", val
            if counter>=1:inc(ans)

    ans
        

        
echo "answer 1: ", ans1(rows,cols)                 

echo "CPU time [ms] ", cpuTime()*1000-t0