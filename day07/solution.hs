#!/usr/bin/env cabal
{- cabal:
build-depends:
    base,
    split,
-}

import Data.List.Split (splitOn)
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
        return (parseLine line : moreInput)

parseLine :: String -> (Int, [Int])
parseLine l = parseSplit $ splitOn ":" l

parseSplit [a, b] = (read a, map read $ words b)

solveA = sum . map fst . filter checkOper

checkOper (s, []) = False
checkOper (s, [a]) = s == a
checkOper (s, a : b : xs) = checkOper (s, a + b : xs) || checkOper (s, a * b : xs)

solveB = sum . map fst . filter checkExtra

checkExtra (s, []) = False
checkExtra (s, [a]) = s == a
checkExtra (s, a : b : xs) = s >= a && (checkExtra (s, a + b : xs) || checkExtra (s, a * b : xs) || checkExtra (s, a `Main.concat` b : xs))

concat a b = read (show a ++ show b)