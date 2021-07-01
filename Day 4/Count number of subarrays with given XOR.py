def total(nums,x):
    n=len(nums)
    count=0
    xor=0
    d={}
    for i in range(n):
        xor^=nums[i]
        if xor^x in d:
            count+=d[xor^x]
        if xor==x:
            count+=1
        if xor in d:
            d[xor]+=1
        else:
            d[xor]=1
    return count
