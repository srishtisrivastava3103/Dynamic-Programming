#nth Fibonacci using Dynamic Programming Tabulation Method (Bottom up Approach or Iterative Method)
F=[-1,-1,-1,-1,-1,-1],
c=0
def fib(n):
    global c
    c+=1
    if n<=1:
        return n
    F[0] = 0
    F[1] = 1
    i = 2
    while(i<=n):
        F[i] = F[i-1]+F[i-2]
        i+=1
    return F[n]
fib(5)
print(c)