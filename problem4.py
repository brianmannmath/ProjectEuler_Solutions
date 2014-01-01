def reverse(string):
    if(string == ''):
        return ''
    else:
        letter = string[0]
        string = string[1:]
        return reverse(string) + letter

num = 1
for i in range(100,1000):
    for j in range(100,1000):
        if(reverse(str(i*j)) == str(i*j)):
            if i*j > num:
                num = i*j
print num
