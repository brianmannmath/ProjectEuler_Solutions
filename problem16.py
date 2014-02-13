#When I wrote this originally, I did not know that Python had support for large
#integers, so I wrote my own functions to do it. This problem could be done in 
#3 lines instead, but I'm going to leave this.

import time

#function which takes a number as a list of digits, multiples the number by 2
#and returns the result as a list
def times_two(list):
    carry = 0
    i=0
    while i < len(list):
        c = list[i]
        list[i] = ((2*list[i] + carry) % 10)
        if (2*c + carry) >= 10:
            carry = 1
            if (i == (len(list)-1)):
                list.append(0)
        else:
            carry = 0
        i = i+1
    return list
#sums the elements of a list            
def list_sum(list):
    if list == []:
        return 0
    else:
        return list.pop() + list_sum(list)
    

t = time.clock()

#sums the digits of 2^1000
digits = [1]

for i in range(1,1001):
    digits = times_two(digits)

print list_sum(digits)

print "computation took", time.clock()-t,"seconds"
