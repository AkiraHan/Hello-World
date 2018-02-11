class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ''
        maxsubstring = ''
        max = 0
        length = 0
        num = 0
        for i in range(len(s)):
            if i == 0:
                substring += s[i]
                length += 1
                if len(s) == 1:
                    max = length
            else:
                if not s[i] in substring:
                    substring += s[i]
                    length += 1
                    if i == len(s)-1 and length > max:
                        maxsubstring = substring
                        max = length
                else:
                    if length > max:
                        maxsubstring = substring
                        max = length
                        for j in range(len(substring)):
                            if substring[j] == s[i]:
                                num = j
                        substring = substring[num+1:] + s[i]
                        length = len(substring)
                    else:
                        for j in range(len(substring)):
                            if substring[j] == s[i]:
                                num = j
                        substring = substring[num+1:] + s[i]
                        length = len(substring)
        return max
