class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max = 0
        for n in range(len(s)):
            substring = ''
            for m in s[n:]:
                if m in substring :
                    if len(substring) > max :
                        max = len(substring)
                    break
                else:
                    substring += m
            if len(substring) > max :
                max = len(substring)
        return max