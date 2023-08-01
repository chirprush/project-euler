-- TODO: This is too slow
import GHC.Float (int2Float)
import Data.List (find)
import Data.Maybe (fromJust)

primeDivisors_ :: [Int] -> Int -> [Int]
primeDivisors_ accum n
  | n <= 1 = accum
  | otherwise = primeDivisors_ (divisor:accum) $ until (\i -> i `mod` divisor /= 0) (`div` divisor) n
  where divisor = fromJust $ find (\i -> n `mod` i == 0) [2..]

primeDivisors :: Int -> [Int]
primeDivisors = primeDivisors_ []

phi :: Int -> Float
phi n = (int2Float n) * (product $ map (\i -> 1.0 - 1.0 / (int2Float i)) $ primeDivisors n)

main :: IO ()
main = print $ sum $ map phi [2..1000000]
