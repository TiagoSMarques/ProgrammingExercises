
import tables

var a = (x:1,y:1)

var b = (x:0,y:2)

var posT = @[(1,0),(2,3)].toTable

posT["2"]=((4,4))
echo posT
# echo abs(b.x-a.x) >= 2 or abs(b.y-a.y)>=2