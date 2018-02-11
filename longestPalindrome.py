class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 0
        length = 0
        LPs = ''
        Befi = 0
        Afti = 0
        if len(s) == 1:
            return s
        for i in range(len(s)):
            if i == 0:
                length = 1
                Befi = i
                Afti = i
                while Afti < len(s)-1 and s[Afti] == s[Afti+1]:
                        Afti += 1
                        length += 1
                max = length
                if Afti != len(s):
                    LPs = s[Befi:Afti+1]
                else:
                    LPs = s
            elif i+1 == len(s):
                pass
            else:
                length = 1
                Befi = i
                Afti = i
                while Afti < len(s)-1 and s[Afti] == s[Afti+1]:
                    Afti += 1
                    length += 1
                while Befi > 0 and Afti < len(s)-1:
                    Befi = Befi -1
                    Afti = Afti +1
                    if s[Befi] != s[Afti]:
                        Befi = Befi +1
                        Afti = Afti -1
                        break
                    length += 2
                if length > max:
                    max = length
                    if Afti != len(s)-1:
                        LPs = s[Befi:Afti+1]
                    else:
                        LPs = s[Befi:]
        return LPs
