class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        Num = 0
        flag = -1
        List = []
        for i in range(numRows):
            List.append([])
        if numRows != 1:
            flag = 0
        for x in s:
            List[Num].append(x)
            if flag == 0 and Num != numRows-1:
                Num += 1
            elif flag == 0 and Num == numRows-1:
                Num -= 1
                flag = 1
            elif flag == 1 and Num != 0:
                Num -= 1
            elif flag == 1 and Num == 0:
                Num += 1
                flag = 0
        Zs = ''
        for i in range(numRows):
            for x in List[i]:
                Zs += x
        return Zs
