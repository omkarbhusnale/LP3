# PR-1  Fibonacci series

#without recursion
l=[0,1]
p=int(input("enter a number:"))

for i in range(p):
    l.append(l[-1]+l[-2])
print(l)



def fib(i):
    if i==1 or i==2:
        return 1
    return fib(i-1)+fib(i-2)

p=int(input("enter a Num:"))
print(fib(p))