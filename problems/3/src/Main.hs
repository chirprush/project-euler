-- If we get all of the divisors of a number by iterating through each
-- number, they're all going to be prime anyway
divisors :: Int -> Int -> [Int] -> [Int]
divisors n divisor accum
  | n == 0 || n == 1 = accum
  | otherwise = case n `mod` divisor == 0 of
    True -> divisors (n `div` divisor) divisor (divisor:accum)
    False -> divisors n (divisor + 1) accum

main :: IO ()
main = print $ maximum $ divisors 600851475143 2 []
