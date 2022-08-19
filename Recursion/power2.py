def power(x, n):
    if(n==0):
        return 1
    partialAns = power(x, (n//2))
    if(n%2 ==1 ):
        return partialAns*partialAns*x
    return partialAns *partialAns 

n = int(input("Enter a number: "))
r = int(input("Enter a number: "))

print(power(n , r))