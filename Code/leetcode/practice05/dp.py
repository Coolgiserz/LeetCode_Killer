class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        # P[i, j]
        if len(s) < 2:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]
        # warning: 不能用下面的方式初始化二维数组，会导致所有行都是同一个引用
        # P = [[0] * len(s)] * len(s)
        P = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            P[i][i] = 1
        max_len = 1
        ii = 0
        for substr_len in range(2, len(s) + 1):
            for i in range(len(s)):
                j = i + substr_len - 1
                if j >= len(s):
                    break
                if s[i] == s[j]:
                    if j - i < 3:
                        P[i][j] = 1
                    else:
                        P[i][j] = P[i + 1][j - 1]
                else:
                    P[i][j] = 0
                if P[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    ii = i
        return s[ii: ii + max_len]



