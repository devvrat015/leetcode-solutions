"""
Problem    : 0005. Longest Palindromic Substring
Link       : https://leetcode.com/problems/longest-palindromic-substring/
Difficulty : Medium
Tags       : Two Pointers, String, Dynamic Programming, Manacher
Runtime    : 222 ms (beats 88.73%)
Memory     : 19.43 MB (beats 18.69%)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)

            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
