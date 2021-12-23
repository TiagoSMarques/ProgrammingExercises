-----------------------Chapter 1------------------------
--Starting out

main :: IO ()
doubleMe :: Num a => a -> a
doubleMe x = x * 2

doubleUs :: Num a => a -> a -> a
doubleUs x y = x * 2 + y * 2

doubleUs2 :: Num a => a -> a -> a
doubleUs2 x y = doubleMe x + doubleMe y

doubleSmallNumber :: (Ord a, Num a) => a -> a
doubleSmallNumber x =
  if x > 100
    then x
    else x * 2

doubleSmallNumber2 :: (Num a, Ord a) => a -> a
doubleSmallNumber2 x = (if x > 100 then x else x * 2) + 1

-- --------------Lists----------------------
xs :: [Integer]
xs = [1, 2, 3, 4, 5, 6, 7, 8]

main = do
  -- --------------List Concatenation: has to iterate over list each time can be slow
  print (xs ++ [2, 4, 3, 9])
  print (xs ++ [5]) -- has to be treated as a list
  print ("Hello" ++ " " ++ "World!!")
  print (['r', 'a'] ++ ['t', 'o']) --strings are just lists of chars
  -- -----------appending something to the beginning of a list - very fast
  print (5 : xs)
  print ('A' : " small cat")
  -- acessing elements os a list !! operator
  print ("Boas malta !" !! 6)
  print ([4.65, 3.65, 2.12] !! 1)
  -- -------------Comparing lists------------------------
  print ([3, 2, 1] > [2, 1, 0])
  print ([3, 2, 1] > [2, 10, 100])
  print ([3, 4, 1] < [3, 4, 2])
  -- -----------------------Basic List functions--------------------
  print (head [1, 2, 3]) -- return the first elem
  print (tail [1, 2, 3]) -- return the rest everything but the first
  print (last [1, 2, 3]) -- return the last elem
  print (init [1, 2, 3]) -- return the the everything but the last
  print (length xs) -- returns the length
  print (null [1, 2]) --checks is list is empty
  print (reverse xs) --reverses a list
  print (take 3 xs) -- extract x elements from a list
  print (drop 3 xs) -- extract elements after the first x elem
  print (maximum xs) -- returns the max value
  print (minimum xs) -- returns the min value
  print (sum xs) -- returns the sum of the elements
  print (product xs) -- returns the product of the elements
  print (4 `elem` [1, 2, 3, 4]) --checks if the elem is in the list
  -- --------------------Ranges------------------------------
  print [1 .. 10]
  print ['a' .. 'f']
  print [3, 6 .. 20] -- specify a step using the first 2 elem
  print [0.1, 0.3 .. 1] -- dont use range with floats
  print (take 5 [1, 5 ..]) --infinite list because no upper limit and shows the first 24 elements
  print (take 10 (cycle [1, 2, 3])) -- cycle a list infinitly
  print (replicate 3 5) -- first 3 number of an infinite list of 5
  -- -----------------Set Comprehension--------------------------
  print ([x * 2 | x <- [1 .. 10]]) -- first 10 even numbers
  print ([x * 2 | x <- [1 .. 10], x * 2 >= 12]) -- we can add a predicate condition
  print ([x | x <- [50 .. 100], x `mod` 7 == 3]) -- all numbers between 50 e 100 that / 7 remainder 3
  print ([x + y | x <- [1, 2, 3], y <- [10, 50, 100], x + y > 15]) -- from 2 lists
  print (sum [1 | _ <- xs]) -- another way to write a length function _ means anything
  -- --------------Tuples------------------
  -- touples are used to write things like vector because a list of a touple of size 2 for example cant contain touples os diferent sizes than 2
  print [(1, 2, 3), (4, 5, 6), (3, 0, 7)] --tuples are fixed size can´t combine them
  print ("Tiago", "Marques", 26) -- example use of a tuple
  -- using pairs (tuples o size 2)
  -- t2 :: (Integer,Integer)
  let t2 = (8, 10)
  print (fst t2) -- takes a pair and returns the first component
  print (snd t2) -- takes a pair and returns the first component
  -- produce tuple pairs
  print (zip [1, 2, 3, 4] [4, 3, 2, 1])
  print (zip [1 ..] ["one", "two", "three", "four", "five"]) -- thanks to lazy eval we can zip infinite lists
