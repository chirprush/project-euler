primes :: [Int]
primes = sieve [2..]
  where sieve (first:rest) = first : sieve (filter (\i -> i `mod` first /= 0) rest)

main :: IO ()
main = print $ primes !! 10000
