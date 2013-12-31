main :: IO ()
main = putStrLn (show (foldr (+) 0 [a | a <- [1..999], (mod a 5) == 0 || (mod a 3) == 0]))

-- Answer is 234168

