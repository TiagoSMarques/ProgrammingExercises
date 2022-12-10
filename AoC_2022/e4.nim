import strutils,sequtils, times
# Simple benchmarking
var t0 = cpuTime()

let data = readFile("4.txt").split("\r\n")

var ans1,ans2=0

for i in 0 ..< data.len:
    let data1=data[i].split(",")
    let elf1=map(rsplit(data1[0],"-"),proc(x: string): int = parseInt(x))
    let elf2=map(rsplit(data1[1],"-"),proc(x: string): int = parseInt(x))

    # chech if one sequence is fully contained in another
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf2[0]<=elf1[0] and elf2[1] >= elf1[1]):
        ans1+=1
    # check if the sequence overlaps anywhere 
    if (elf2[1] >= elf1[0] and elf1[1]>=elf2[0]) or (elf1[1] >= elf2[0] and elf2[1]>=elf1[0]):
        ans2+=1



echo "CPU time [s] ", cpuTime()-t0
echo "ans1: ",ans1, " ans2: ", ans2