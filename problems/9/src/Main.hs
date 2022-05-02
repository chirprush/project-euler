-- This uses Euclid's formula for generating Pythagorean triples:
-- https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
findTriple :: Int -> Int -> ((Int, Int, Int), Int)
findTriple m n
  | n >= m = findTriple (m + 1) 1
  | sum > 1000 = findTriple (m + 1) 1
  | sum < 1000 = findTriple m (n + 1)
  | sum == 1000 = ((a, b, c), a * b * c)
  where (a, b, c) = (m ^ 2 - n ^ 2, 2 * m * n, m ^ 2 + n ^ 2)
        sum = a + b + c

main :: IO ()
main = print $ findTriple 2 1
