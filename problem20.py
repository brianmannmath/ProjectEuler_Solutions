import time

#adds two list-numbers
def add(list_one,list_two):
    carry = 0
    i = 0
    sum = [0]
    #need list_one to be longer
    if(len(list_one) < len(list_two)):
        t = list_one
        list_one = list_two
        list_two = t
    for num in range(len(list_two),len(list_one)+1):
        list_two.append(0)
    while i < len(list_one):
        sum.append(0)
        sum[i] = (list_one[i] + list_two[i] + carry) % 10
        if (list_one[i] + list_two[i] + carry < 10):
            carry = 0
        else:
            carry = 1
            if i == len(list_one)-1:
                sum[i+1] = 1
        i = i+1
    return sum
        
    
    
#multiplies a number by a list-number
def mult(n,num_list):
    sum = num_list
    for num in range(1,n):
        sum = add(num_list,sum)
    return sum
    
#sums the elements of a list            
def list_sum(list):
    if list == []:
        return 0
    else:
        return list.pop() + list_sum(list)
    

t = time.clock()

list = [1]
for j in range(2,101):
    list = mult(j,list)
    while list[len(list)-1] == 0:
        c = list.pop()

print list_sum(list)

print "computation took", time.clock()-t,"seconds"
