class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        for x in range(len(s)):
            for y in range(len(s[x:])+x,0,-1):
                substring = s[x:y]
                if len(substring) < len(answer):
                    break

                if substring == substring[::-1]:
                    if len(substring) > len(answer):
                        answer = substring

        return answer