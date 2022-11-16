n = print(input('Enter weight'))
a = print(input('A\'s share'))
b = print(input('B\'s share'))
a = int(a)
b = int(b)

q = a + b

if a % 2 == 0 and b % 2 == 0:
    if q < n or q == n:
        print('Yes, Watermelon can be divided into two parts')
    else :
        print('No, Watermelon cannot be divided into two parts')
elif a % 2 != 0 and b % 2 != 0:
    print('No, Watermelon cannot be divided into two parts')