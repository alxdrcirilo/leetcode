class Solution:
    def reverseWords(self, s: str) -> str:
        string = s.split()
        string.reverse()
        return " ".join(string)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
    ]

    for s, expected in test_cases:
        assert solution.reverseWords(s) == expected
