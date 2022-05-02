import qualified Data.Map.Strict as Map

divisors' :: Int -> Int -> Map.Map Int Int -> Map.Map Int Int
divisors' n divisor divs
  | n == 0 || n == 1 = divs
  | otherwise = case n `mod` divisor == 0 of
    True -> divisors' (n `div` divisor) divisor $ Map.insertWith (\_ old -> old + 1) divisor 1 divs
    False -> divisors' n (divisor + 1) divs

divisors :: Int -> Map.Map Int Int
divisors n = divisors' n 2 Map.empty

main :: IO ()
main = print $ Map.foldrWithKey (\base exp accum -> accum * base ^ exp) 1 $ foldr1 (Map.unionWith max) $ map divisors [2..20]
