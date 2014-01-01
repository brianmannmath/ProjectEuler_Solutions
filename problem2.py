first = 1
second = 1
term = 0
sum = 0

while second < 4000000:
    if (second % 2 == 0):
        sum = sum + second
    term = first + second
    first = second
    second = term
print sum
