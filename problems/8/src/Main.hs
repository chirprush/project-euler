import Data.Char (digitToInt, isSpace)

frameProduct :: String -> Int
frameProduct frame = product $ map digitToInt frame

greatestProduct :: String -> Int -> Int -> Int
greatestProduct input index biggest
  | index + 13 >= length input = biggest
  | otherwise = greatestProduct input (index + 1) (max product biggest)
    where frame = take 13 $ drop index input
          product = frameProduct frame

main :: IO ()
main = do
  input' <- readFile "input.txt"
  let input = filter (not . isSpace) input'
  print $ greatestProduct input 0 0
