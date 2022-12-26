import strutils, sequtils, times

var t0 = cpuTime()*1000

var posT = @[(x:0,y:0)]
var posH : tuple[x:int,y:int]
let dir = (L:(-1,0), R:(1,0), U:(0,1), D:(0,-1))

proc addTupple(a,b: (int,int)): (int,int) = (a[0]+b[0],a[1]+b[1])
    

proc moveTail(h:tuple[x:int,y:int], dir:(int,int)): void =

    var tail = posT[^1]

    if abs(tail.x-h.x)>=2 or abs(tail.y-h.y)>=2: 
        if h.x == tail.x or h.y == tail.y:
            posT.add(addTupple(tail,dir))
        if  h.x < tail.x and h.y < tail.y:
            posT.add(addTupple(tail,(-1,-1)))
        if  h.x < tail.x and h.y > tail.y:
            posT.add(addTupple(tail,(-1,1)))
        if  h.x > tail.x and h.y < tail.y:
            posT.add(addTupple(tail,(1,-1)))
        if  h.x > tail.x and h.y > tail.y:
            posT.add(addTupple(tail,(1,1)))
    
var data = readFile("9.txt").split("\r\n")

for l in data:
    var instr=l.split(" ")
    for i in 1..parseInt(instr[1]):
        case instr[0]:
            of "L":
                posH = addTupple(posH,dir.L)
                moveTail(posH,dir.L)
            of "R":
                posH = addTupple(posH,dir.R)
                moveTail(posH,dir.R)
            of "U":
                posH = addTupple(posH,dir.U)
                moveTail(posH,dir.U)
            of "D":
                posH = addTupple(posH,dir.D)
                moveTail(posH,dir.D)


echo "Answer 1: ", posT.deduplicate().len

echo "CPU time [ms] ", cpuTime()*1000-t0


