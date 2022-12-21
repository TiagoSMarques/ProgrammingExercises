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

# Criar a matriz do tabuleiro de jogo 
for x, row in rows:
    # separar as linhas pelo nm total de colunas
    var rowSep = toSeq(row[0].items).distribute(nCols)
    for y,val in rowSep:
        # adicionar só a info relevante à matrix
        if $val[1] != " ":
            Board[y].addlast($val[1])


# Criar a lista de instruções
let instRaw=data[1].split("\r")
var instr : seq[array[3,string]]

for ind,step in instRaw:
    let temp = step.split(" ")
    instr.add([temp[1],temp[3],temp[5]])

var Board1 = Board
var Board2= Board

proc ans1(boardData: var seq[Deque[string]], instrData:seq[array[3,string]]): string =
    #Aplicar os movimentos
    for step in instrData:

        let quant = parseInt($step[0])
        let fromCol= parseInt($step[1]) - 1
        let toCol=parseInt($step[2]) - 1

        for i in 1..quant:
            boardData[toCol].addFirst(peekFirst(boardData[fromCol]))
            boardData[fromCol].popFirst()

    #Compute answer 1 
    var ans : seq[char]
    for l in 0..nCols-1:
        ans.add(boardData[l].peekFirst())

    ans.join
    

proc ans2(boardData: var seq[Deque[string]], instrData:seq[array[3,string]]): string =
    #Aplicar os movimentos
    for step in instrData:

        let quant = parseInt($step[0])
        let fromCol= parseInt($step[1]) - 1
        let toCol=parseInt($step[2]) - 1

        for i in countdown(quant,1):
            boardData[toCol].addFirst(boardData[fromCol][i-1])
            
        for i in 1..quant: boardData[fromCol].popFirst

    #Compute answer 1 
    var ans : seq[char]
    for l in 0..nCols-1:
        ans.add(boardData[l].peekFirst())

    return ans.join


echo "Answer 1: ", ans1(Board1,instr)
echo "Answer 2: ", ans2(Board2,instr)


echo "CPU time [ms] ", cpuTime()*1000-t0