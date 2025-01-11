class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        i = 0
        for j in range(len(t)):
            if s[i] == t[j]:
                i += 1
            if i == len(s):
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("", "ahbgdc", True),
    ]
    for s, t, expected in test_cases:
        assert solution.isSubsequence(s, t) == expected
