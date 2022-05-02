import Data.List (unfoldr)

fibs :: [Int]
fibs = unfoldr nextFib (0, 1)
  where nextFib state
            | total > 4000000 = Nothing
            | otherwise = Just (total, (snd state, total))
            where total = fst state + snd state

main :: IO ()
main = print $ sum $ filter (\a -> a `mod` 2 == 0) fibs
