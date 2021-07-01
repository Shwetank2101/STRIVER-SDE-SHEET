def maxarr(nums):
    d={}
    cmax=0
    csum=0
    for i in range(len(nums)):
        csum+=nums[i]
        if csum==0 and cmax==0:
            cmax=1
        if csum==0:
            cmax=i+1
        if csum in d:
            cmax=max(cmax,i-d[csum])
        else:
            d[csum]=i
    return cmax
