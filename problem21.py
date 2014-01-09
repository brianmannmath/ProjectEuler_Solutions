import time



#function for finding the sum of the divisors of n
def sum_of_div(n):
    s = 0
    for num in range(1,int(n/2+1)):
        if n % num == 0:
            s = num + s
    return s  

t = time.clock()

d = dict()

for num in range(1,10000):
    sum = sum_of_div(num)
    if (num in d):
        continue
    elif num != sum and sum_of_div(sum) == num:
        d[num] = sum
        d[sum] = num

s =0       
for i in iter(d):
    s = s + i

print s

print "computation took", time.clock()-t,"seconds"
