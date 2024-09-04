class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_len = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                flag = self.has_repeated_char(s[i:j])
                if flag:
                    continue
                else:
                    if len(s[i:j]) > max_len:
                        max_len = len(s[i:j])
        return max_len

    def has_repeated_char(self, s: str) -> bool:
        charset = set()
        for ch in s:
            if ch in charset:
                return True
            else:
                charset.add(ch)
        return False
