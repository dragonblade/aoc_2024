#!/usr/bin/env cabal
{- cabal:
build-depends:
    base,
    regex-pcre,
    universe-base,
-}

import Data.List (sort, transpose)
import Data.Universe.Helpers (diagonals)
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

solveA l = sum (map matchXmas l) + sum (map matchXmas $ transpose l) + sum (map matchXmas $ diagonals l) + sum (map matchXmas $ diagonals $ map reverse l)

matchXmas :: String -> Int
matchXmas s = length (s =~ "XMAS" :: [[String]]) + length (s =~ "SAMX" :: [[String]])

solveB = solveBh 1 1

solveBh y x g
  | x == length (head g) - 1 = solveBh (y + 1) 1 g
  | y == length g - 1 = 0
  | otherwise = fromEnum (checkXmas g y x) + solveBh y (x + 1) g

checkXmas :: [String] -> Int -> Int -> Bool
checkXmas g y x =
  y < length g - 1
    && x < length (head g) - 1
    && g !! y !! x == 'A'
    && sort [g !! (y - 1) !! (x - 1), g !! (y + 1) !! (x + 1)] == ['M', 'S']
    && sort [g !! (y - 1) !! (x + 1), g !! (y + 1) !! (x - 1)] == ['M', 'S']
