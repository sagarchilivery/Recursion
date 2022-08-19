def fac(n):
    if(n == 0):
        return 1
    intermediate = fac(n-1)
    return n *intermediate 
n = int(input("Enter a number: "))
print(fac(n))
