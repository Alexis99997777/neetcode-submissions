class Solution:
    def longestPalindrome(self, s: str) -> str:
        #interval dp
        #edge case
        if not s:
            return ""
        
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        #init
        for i in range(n):
            dp[i][i] = True
        
        start = 0
        best_length = 1
        #ababd
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    length = j - i + 1
                    if length > best_length:
                        best_length = length
                        start = i
        return s[start:start + best_length]
