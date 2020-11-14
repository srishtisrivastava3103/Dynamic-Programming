#Dynamic programming works for optimization problems using principle of optimality(A problem must be solved in sequence of decisions)
#Dynamic Programming: 5th digit of Fibonacci using Memoization (Top Down Approach)
F = [-1,-1,-1,-1,-1,-1]
c = 0 # Here c gives the number of function calls.
def fib1(n):
    global c
    c+=1
    if n <= 1:
        return n
    if F[n-2] == -1:
        F[n-2] = fib(n-2)
    k = F[n-2]
    if F[n-1] == -1:
        F[n-1] = fib(n-1)
    j = F[n-1]
    F[n] = k + j
    return F[n]
fib1(5)
print(F)
print("No of function calls: "+str(c))


    
    
    