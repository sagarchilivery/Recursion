n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

def power(n, r):
    if(r==0):
        return 1
    partialAns = power(n, r-1)
    return n*partialAns


print(power(n1, n2))