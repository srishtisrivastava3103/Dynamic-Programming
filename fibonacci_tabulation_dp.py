#Recursive method for the same question (without Dynamic Programming)
c = 0
def fib(n):
    global c
    c+=1
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)
fib(5)
print("No of function calls: "+str(c))
