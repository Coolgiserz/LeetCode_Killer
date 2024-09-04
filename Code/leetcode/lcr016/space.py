class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        滑动窗口
        遍历子串索引i，j，[i,j)为滑动窗口
        """
        if len(s) < 2:
            return len(s)
        max_len = 0
        rk = -1
        _set = set()
        for i, ch in enumerate(s):
            if i > 0:
                _set.remove(s[i-1])
            while rk+1< len(s) and s[rk+1] not in _set:
                _set.add(s[rk+1])
                rk += 1
            max_len = max(rk-i+1, max_len)
        return max_len