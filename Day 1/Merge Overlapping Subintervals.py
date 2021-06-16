class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        out=intervals[0]
        s=[]
        for i in range(n):
            temp=intervals[i]
            if temp[0]<=out[1]:
                out[1]=max(temp[1],out[1])
            else:
                s.append(out)
                out=temp
        s.append(out)
        return s
            
        
