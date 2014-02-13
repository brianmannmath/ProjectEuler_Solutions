part = [1,1,2]

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

    part.append(val % 1000000)

print(len(part)-1, part[len(part)-1])
