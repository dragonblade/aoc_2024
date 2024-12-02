#!/usr/bin/env cabal
{- cabal:
build-depends:
    base,
-}

import System.IO (isEOF)

main = do
  input <- readInput
  print (solveA input)
  print (solveB input)

readInput =
  do
    done <- isEOF
    if done
      then return []
      else do
        line <- getLine
        moreInput <- readInput
        return (map read (words line) : moreInput)

solveA = foldr ((\b acc -> if b then acc + 1 else acc) . checkSafe) 0

checkSafe [] = True
checkSafe [_] = True
checkSafe (a : b : r) = if a > b then loopSafe (>) (a : b : r) else loopSafe (<) (a : b : r)

loopSafe op [] = True
loopSafe op [_] = True
loopSafe op (a : b : r) = isSafe op a b && loopSafe op (b : r)

isSafe op a b = a `op` b && 1 <= abs (a - b) && abs (a - b) <= 3

solveB = foldr ((\b acc -> if b then acc + 1 else acc) . checkForgiving []) 0

checkForgiving l [] = False
checkForgiving l [_] = False
checkForgiving l (a : b : r) = checkSafe (l ++ (a : r)) || checkSafe (l ++ (b : r)) || checkForgiving (l ++ [a]) (b : r)