def sort(l1,l2):
    i,j=0,0
    n1=len(l1)
    n2=len(l2)
    while i<n1:
        if l2[j]>l1[i]:
            i+=1
        else:
            l2[j],l1[i]=l1[i],l2[j]
            i+=1
            for k in range(j,n2):
                if l2[j]>l2[k]:
                    l2[j],l2[k]=l2[k],l2[j]
        print(*l1,*l2)
    print(*l1,*l2)
