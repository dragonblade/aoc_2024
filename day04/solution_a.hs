#!/usr/bin/env cabal
{- cabal:
build-depends:
    base,
    regex-pcre,
    universe-base,
-}

import Data.List (transpose)
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

solveB [] = 0
solveB [_] = 0
solveB [_, _] = 0
solveB (a : b : c : xs) = matchXMas (concat [a, b, c]) (length a) + solveB (b : c : xs)

matchXMas :: String -> Int -> Int
matchXMas s l =
  length (s =~ ("M.S.{" ++ show (l - 2) ++ "}A.{" ++ show (l - 2) ++ "}M.S") :: [[String]])
    + length (s =~ ("M.S.{" ++ show (l - 2) ++ "}A.{" ++ show (l - 2) ++ "}S.M") :: [[String]])
    + length (s =~ ("S.M.{" ++ show (l - 2) ++ "}A.{" ++ show (l - 2) ++ "}M.S") :: [[String]])
    + length (s =~ ("S.M.{" ++ show (l - 2) ++ "}A.{" ++ show (l - 2) ++ "}S.M") :: [[String]])
