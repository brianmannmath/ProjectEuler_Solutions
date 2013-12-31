-- Find the sum of the even terms of the Fib seq less than 4 million

fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)

fiblist :: [Int]
fiblist = 1:1:zipWith (+) fiblist (tail fiblist)

x :: [Int]
x = (takeWhile (<4000000) fiblist)

f :: Int
f = (foldr (+) 0 [a | a <- x,(mod a 2 == 0)])

main :: IO ()
main = putStrLn (show f)


--Answer is 4613732