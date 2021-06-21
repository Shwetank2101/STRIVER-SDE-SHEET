class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1,count2,x,y=0,0,0,1
        for i in nums:
            if x==i:
                count1+=1
            elif y==i:
                count2+=1
            elif count1==0:
                count1,x=1,i
            elif count2==0:
                count2,y=1,i
            else:
                count1-=1
                count2-=1
        c1=c2=0
        for i in nums:
            if i==x:
                c1+=1
            elif i==y:
                c2+=1
        out=[]
        n=len(nums)
        if c1>n/3:
            out.append(x)
        if c2>n/3:
            out.append(y)
        return out
