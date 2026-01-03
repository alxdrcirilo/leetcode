class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        while i < len(haystack):
            if haystack[i : i + len(needle)] == needle:
                return i
            i += 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    assert solution.strStr("sadbutsad", "sad") == 0
    assert solution.strStr("leetcode", "leeto") == -1
    assert solution.strStr("hello", "ll") == 2
