def square(n):
    if n==1:
        return 1
    x=n>>1
    if n&1:
        return ((square(x)<<2) + (x<<2) + 1)
    else:
        return (square(x)<<2)

    
