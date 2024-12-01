#!/usr/bin/env cabal
{- cabal:
build-depends:
    base,
    containers,
default-extensions:
    ImportQualifiedPost,
-}

import Data.List (sort)
import Data.Map qualified as Map
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

parseLine = convertLine . map read . words

convertLine [a, b] = (a, b)

solveA = sum . map absDiff . sortMatrix

sortLists (a, b) = (sort a, sort b)

sortMatrix :: Ord a => [(a, a)] -> [(a, a)]
sortMatrix = uncurry zip . sortLists . unzip

absDiff (a, b) = abs $ a - b

solveB = solveBa . unzip

solveBa (l, r) = computeSim l $ buildMap r

computeSim l m = sum $ map (\x -> Map.findWithDefault 0 x m) l

buildMap a = Map.fromListWith (+) $ map makeTuple a

makeTuple a = (a, a)