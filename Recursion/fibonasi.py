def fib(n):
    if(n ==1):
        return 1
    if(n ==2):
        return 1
    partialAns1= fib(n-1)
    partialAns2= fib(n-2)
    return partialAns1+partialAns2

n = int(input("Enter a number: "))
print(fib(n))