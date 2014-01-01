#prime test function
def isprime(n):
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3,int(n**0.5 + 1),2):
        if (n % i == 0):
            return False
    return True

#largest prime factor
factor = 1

for num in range(2,int(600851475143**0.5 + 1)):
    if (600851475143 % num == 0):
        if isprime(num) == True:
            factor = num
print factor

