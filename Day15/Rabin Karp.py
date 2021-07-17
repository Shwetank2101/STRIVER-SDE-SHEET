def asci(s):
    return ord(s)-ord('a')+1
def check(s,t):
    m=len(s)
    for i in range(m):
        if s[i]!=t[i]:
            return 0
    return 1
def search(s,t):
    x=100
    #base=10**10
    if s=='' or t=='':
        return -1
    m=len(t)
    n=len(s)
    target=0
    current=0
    for i in range(m):
        #target=(target*x+asci(t[i]))%base
        #current=(current*x+asci(s[i]))%base
        #print(target)
        target=(target*x+asci(t[i]))
        current=(current*x+asci(s[i]))
    for i in range(n-m+1):
        if target==current:
            if check(s[i:i+m],t):
                print('Pattern found at',i)
        current=current-(x*m*asci(s[i]))+(x*m*asci(s[i+m-1]))
        #current=(current-(x*m*asci(s[i]))+(x*m*asci(s[i+m-1])))%base
