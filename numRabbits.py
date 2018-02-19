class Solution:
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if(len(answers) == 0):
            return 0
        answers.sort()
        res = 0
        i = 0
        while i < len(answers):
            num = answers[i]
            res += (num + 1)
            while num > 0 and i+1 < len(answers) and answers[i+1] == answers[i]:
                i += 1
                num -= 1
            i += 1
        return res
        
