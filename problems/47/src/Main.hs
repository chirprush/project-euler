import Data.List (find, elemIndex)
import Data.Maybe (fromJust)

primeDivisors_ :: Int -> Int -> Int -> Int
primeDivisors_ start accum n
  | n <= 1 = accum
  | otherwise = primeDivisors_ (divisor + 1) (accum + 1) $ until (\i -> i `mod` divisor /= 0) (`div` divisor) n
  where divisor = fromJust $ find (\i -> n `mod` i == 0) [start..] -- Somehow change this to only include odds except for 2?

primeDivisors :: Int -> Int
primeDivisors n = primeDivisors_ 2 0 n

fourDistinctPrimes :: Int -> Int
fourDistinctPrimes n
  | and consecutives = n
  | otherwise = fourDistinctPrimes $ n + 4 - (fromJust $ elemIndex False $ reverse consecutives)
  where consecutives = map ((== 4) . primeDivisors . (+ n)) [0..3]

main :: IO ()
main = print $ fourDistinctPrimes 2
