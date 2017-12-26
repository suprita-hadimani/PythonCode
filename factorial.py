def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)
z=int(input("enter the number"))
print (fact(z))
