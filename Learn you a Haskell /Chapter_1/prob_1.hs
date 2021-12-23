main :: IO ()
-- ------Problem--------
-- length of triangle is an int
-- length of each side < 10
-- sum of len = 24
-- right triangle
-- a²+b²=c²

-- the standard aproach is to start with a set of candidates then filter them down through tranformations and filters

triples :: [(Integer, Integer, Integer)]
triples =
  [ (a, b, c)
    | c <- [1 .. 10],
      b <- [1 .. c],
      a <- [1 .. b], -- change the list range to make c the hipothenuse and b > a
      a ^ 2 + b ^ 2 == c ^ 2,
      a + b + c == 24
  ]
main = do
  print triples