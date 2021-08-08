
def meeting(nums):
    out=[]
    for i in range(len(nums)):
        out.append(nums[i]+[i+1])
    out.sort(key=lambda x:x[1])
    res=[out[0][-1]]
    curr=out[0][-2]
    for i in range(1,len(out)):
        if curr<out[i][0]:
            res.append(out[i][-1])
            curr=out[i][0]
    print(*res)
l=[]
for i in range(int(input())):
    l.append(list(map(int,input().split())))
meeting(l)
