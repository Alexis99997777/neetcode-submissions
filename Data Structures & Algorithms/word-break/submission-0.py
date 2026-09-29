class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        wordDict = set(wordDict)
        max_length = float('-inf')
        for word in wordDict:
            max_length = max(max_length,len(word))


        dp = [False] * (n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(max(0,i-max_length),i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]