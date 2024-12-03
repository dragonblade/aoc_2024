#!/usr/bin/env cabal
{- cabal:
build-depends:
    base,
    regex-pcre,
default-extensions:
    FlexibleContexts,
-}

import System.IO (isEOF)
import Text.Regex.PCRE ((=~))

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
        return (line : moreInput)

solveA :: [String] -> Integer
solveA = sum . map compute . concatMap matchA

matchA l = l =~ "mul\\((\\d+),(\\d+)\\)" :: [[String]]

compute [_, a, b] = read a * read b

solveB = loop True . concatMap matchB

matchB l = l =~ "mul\\((\\d+),(\\d+)\\)|do\\(\\)|don\'t\\(\\)" :: [[String]]

loop e [] = 0
loop e (x : xs)
  | head x == "do()" = loop True xs
  | head x == "don't()" = loop False xs
  | otherwise = (if e then compute x else 0) + loop e xs