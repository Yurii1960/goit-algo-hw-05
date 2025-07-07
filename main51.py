def caching_fibonacci():
    cash={}
    def fibonacci(n):
        if n<=0:
            return 0
        if n==1:
            return 1
        if n in cash:
            #print(n)
            return cash[n]
        else:
            cash[n]=fibonacci(n-2)+fibonacci(n-1)
            return cash[n]
    return fibonacci
fib=caching_fibonacci()
print(fib(10))
print(fib(15))