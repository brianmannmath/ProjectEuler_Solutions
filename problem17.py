#How many letters are used writting out the numbers 1 to 1000 inclusive?

ones = dict([('one',3),('two',3),('three',5),('four',4),('five',4),('six',3),('seven',5),('eight',5),('nine',4)])

special = dict([('ten',3),('eleven',6),('twelve',6),('thirteen',8),('fourteen',8),('fifteen',7),('sixteen',7),('seventeen',9),('eighteen',8),('nineteen',8)])

tens = dict([('twenty',6),('thirty',6),('forty',5),('fifty',5),('sixty',5),('seventy',7),('eighty',6),('ninety',6)])

#numbers are of the form 'tens'-'ones' or 'ones'-'hundred'-'and'-'tens'-'ones'
#count 'tens'-'ones' first:

def sum_of_class(dic):
    total = 0
    for key in dic:
        total += dic[key]

    return total

under_one_hundred = sum_of_class(ones) + sum_of_class(special) + sum_of_class(tens) + sum_of_class(tens)*9 + sum_of_class(ones)*8

others = 11 + (sum_of_class(ones) + 7*9) + 99*(13 + 13 + 15 + 14 + 14 + 13 + 15 + 15 + 14) + under_one_hundred*9

print(under_one_hundred + others)

