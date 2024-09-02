def longestPalindrome(s: str) -> str:
    """
    暴力解法
    >>> longestPalindrome('babad')
    'bab'
    >>> longestPalindrome('cbbd')
    'bb'
    >>> longestPalindrome('a')
    'a'
    >>> longestPalindrome('ac')
    'a'
    """
    if len(s)==1:
        return s
    if len(s)==2:
        if s[0]==s[1]:
            return s
        return s[0]
    max_len = 0
    max_str = ""
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if isPalindrome(s[i:j+1]):
                if j-i+1>max_len:
                    max_len = j-i+1
                    max_str = s[i:j+1]
    return max_str

def isPalindrome(s: str) -> bool:
    """
    >>> assert isPalindrome('aba')==True
    >>> assert isPalindrome('ab')==False
    """
    if len(s)==1:
        return True
    p1 = 0
    p2 = len(s)-1
    while p1 < p2:
        if s[p1]!=s[p2]:
            return False
        p1 += 1
        p2 -= 1
    if p1 == p2:
        return True
    if p2>=0 and s[p1]==s[p2]:
        return True
    return False

# cases = ["aba", "a", "ab", "", "asasaaaa", "bb", "babab"]
# for case in cases:
#     print(case, isPalindrome(case), longestPalindrome(case))


class Solution:

    def longestPalindrome(self, s: str) -> str:
        # 暴力解法
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        max_len = 0
        ii, jj = 0, 0
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if not self.isPalindrome(s[i:j + 1]):
                    continue
                else:
                    if j - i >= max_len:
                        max_len = j - i
                        ii = i
                        jj = j
        return s[ii:jj + 1]

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        if p1 == p2:
            return True
        if p2 >= 0 and s[p1] == s[p2]:
            return True
        return False

solution = Solution()
