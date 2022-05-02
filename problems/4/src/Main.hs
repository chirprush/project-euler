reflectNum :: Int -> Int
reflectNum n = n * 1000 + n `mod` 10 * 100 + (n `mod` 100 `div` 10) * 10 + (n `mod` 1000 `div` 100)

palindromeDivisor :: Int -> (Int, Int)
palindromeDivisor n
  | length divided > 0 = (maximum divided, palin `div` (maximum divided))
  | otherwise = palindromeDivisor $ n - 1
  where palin = reflectNum n
        divided = filter (\a -> palin `mod` a == 0 && palin `div` a < 1000) [100..999]

main :: IO ()
main = print $ palindromeDivisor 999
