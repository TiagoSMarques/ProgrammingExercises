import strutils,times,sequtils, re

# Simple benchmarking
var t0 = cpuTime()*1000

#splitLines()

let data = readFile("5.txt").split("\n\n")

# var piles = data[0].split("\n\n")[0].split("\n")
var piles = splitLines(data[0].split("\n\n")[0])


#---------Parse the Piles --------------------
# determinar o numero de colunas 
var numCols = piles[^1].strip().filterIt(it isnot Natural)[^1]
# criar a tabela de posições 
var table = newSeqWith(piles.len-1, newSeq[string]())
# contar até ao penultimo elem da lista
for i,row in piles[0..^2]:
    # separar todos os caracteres da linha e distribuir pelo num de colunas
    var rowVals = (row.split({' ', '[',']'}).distribute(parseInt($numCols)))
    # Criar a tablela com os valores em cada linha e coluna table[row][col]
    for item in rowVals:
        table[i].add(@[foldl(item, a & b)])


echo "val: ", table[1][0]

#---------Parse the Instructions --------------------
let instr = data[1].split("\n\n")[0].split("\n")

# var input1= instr[0].match(re"\d+").mapIt(parseInt(it))
var matches: array[3, string]
var move=0

for l,line in instr:
    if match(instr[l], re"move (\d) from (\d) to (\d)", matches):

        var quant = parseInt(matches[0])
        var startPile = parseInt(matches[1])
        var endPile = parseInt(matches[2])

        # echo "----",matches
        for box in 0..<quant:
            table[box][endPile-1]=table[box][startPile-1]
            table[box][startPile-1]=""
            move+=1
            # echo move

        echo table





echo "CPU time [ms] ", (cpuTime()*1000 - t0).formatFloat(ffDecimal, 3)

