
n = 4000000
fib_array = []
num1 = 0
num2 = 1
nextnum = num2

while nextnum <= n:
    #print(nextnum, end = " ")
    num1 = num2
    num2 = nextnum
    nextnum = num1+num2
    if nextnum % 2 == 0:
        fib_array.append(nextnum)
    

print(sum(fib_array))

