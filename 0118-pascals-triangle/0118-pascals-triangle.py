class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if i == 0:
                res.append([1])
                continue
            if i == 1:
                res.append([1,1])
                continue
            tmp = [1]
            for j in range(0,len(res[-1])-1):
                tmp.append(res[i-1][j] + res[i-1][j+1])
            tmp.append(1)
            res.append(tmp)
        return res