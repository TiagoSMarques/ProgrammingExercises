import strutils,sequtils, times, deques
# Simple benchmarking
var t0 = cpuTime()*1000

let data = readFile("5.txt").split("\r\n\r")
var tower=data[0].split("\r\n")
var nCols = parseInt($tower[^1].filterIt(it != ' ')[^1])
tower.delete(tower.len-1)
let nRows= tower.len #8 rows

var rows = tower.distribute(nRows)
var Board=  newSeqWith(nCols,initDeque[string](nRows))
# echo "------------------------------------"
# Criar a matriz do tabuleiro de jogo 
for x, row in rows:
    # echo x, row
    # separar as linhas pelo nm total de colunas
    var rowSep = toSeq(row[0].items).distribute(nCols)
    for y,val in rowSep:
        # adicionar só a info relevante à matrix
        if $val[1] != " ":
            # echo y
            Board[y].addlast($val[1])
            # echo y, " : ",Board[y]

# echo Board

# Criar a lista de instruções
let instRaw=data[1].split("\r")
var instr : seq[array[3,string]]

for ind,step in instRaw:
    let temp = step.split(" ")
    instr.add([temp[1],temp[3],temp[5]])

#Aplicar os movimentos
for step in instr:
    let quant = parseInt($step[0])
    let fromCol= parseInt($step[1])
    let toCol=parseInt($step[2])

    for i in 1..quant:
        Board[toCol-1].addFirst(peekFirst(Board[fromCol-1]))
        Board[fromCol-1].popFirst()

# echo Board

#Compute answer 1 
var ans : seq[char]
for l in 0..nCols-1:
    ans.add(Board[l].peekFirst())
    
echo "Answer: ", ans.join
echo "CPU time [ms] ", cpuTime()*1000-t0