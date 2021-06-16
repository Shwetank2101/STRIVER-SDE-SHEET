class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out=[[1],[1,1]]
        if numRows==1 or numRows==2:
            return out[:numRows]
        for i in range(numRows-2):
            temp=[1]
            l=out[i+1]
            for j in range(i+1):
                temp.append(l[j]+l[j+1])
            temp.append(1)
            out.append(temp)
        return out
