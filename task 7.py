n=int(input())
def fibonacci(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(n))

