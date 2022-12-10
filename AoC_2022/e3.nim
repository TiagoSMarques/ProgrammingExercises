import strutils,sequtils, times
# Simple benchmarking
var t0 = cpuTime()

# transform the char into int 
proc toNum(com:char):  int =
  let prior = ord(com)
  if prior <= 90:
    return (prior - 38)
  else:
    return (prior - 96)
  

let data = readFile("3.txt").split("\r\n")
var matches : seq[int]


for i in 0 ..< data.len:
  let sack = data[i]
  # split the bag in half
  let comp1 = sack[0 ..< sack.len div 2]
  let comp2 = sack[sack.len div 2 ..< sack.len]
  #iteratie over the bag and check if an item is in both halves
  for l in 0 ..< comp1.len:
    let item1 = comp1[l]
    if comp2.contains(item1):
      matches.add(toNum(item1))
      #exit as soon as found
      break

let ans1 = matches.foldl(a + b)
echo ans1

# part 2 -------------------
var ans2=0
# split data into groups of 3
for i in countup(0,data.len-3,3):
  var s1 : seq[char]
  var group = data[i..i+2]
  let g0=group[0]
  let g1 =group[1]
  let g2=group[2]
  # check if item form elf1 is in 2 and save the matches
  for p in 0 ..< g0.len:
    let it = g0[p]
    if g1.contains(it):
      s1.add(it)
  # check if item from the matches is in elf 3
  for p1 in 0 ..< s1.len:
    let it2 = s1[p1]
    if g2.contains(it2):
      # add the answers for all groups
      ans2+=toNum(it2)
      # exit when found 
      break

echo ans2

echo "CPU time [s] ", cpuTime() - t0
    
