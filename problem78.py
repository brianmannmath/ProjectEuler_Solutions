#list of numbers of partitions, starting with p(0) = 1
part = [1,1,2]

#Uses Euler's recursion to find p(n)
while (part[len(part)-1] % 1000000 != 0):
    val = 0
    k = 1
    n = len(part)

    while (n >= (k*(3*k-1))/2):
        val = val + ((-1)**(k-1))*part[int(n-(k*(3*k-1))/2)]
        k = k+1

    k = -1
    while (n >= (k*(3*k-1))/2):
        val = val + ((-1)**(k-1))*part[int(n-(k*(3*k-1))/2)]
        k = k-1

    #only need to keep the last 7 digits, since we're only adding
    #remember, if a % m = 0 and b % m = 0 then a + b % m = 0 !!!!
    part.append(val % 1000000)

print(len(part)-1, part[len(part)-1])
