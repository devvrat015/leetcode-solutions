"""
Problem    : 0006. Zigzag Conversion
Link       : https://leetcode.com/problems/zigzag-conversion/
Difficulty : Medium
Tags       : String
Runtime    : 10 ms (beats 56.08%)
Memory     : 19.32 MB (beats 47.15%)
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        direction = 1

        for char in s:
            rows[row] += char

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(rows)
