class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(abs(sum(ord(i) for i in s) - sum(ord(j) for j in t)))


if __name__ == "__main__":
    solution = Solution()
    assert solution.findTheDifference("abcd", "abcde") == "e"
    assert solution.findTheDifference("", "y") == "y"
    assert solution.findTheDifference("a", "aa") == "a"
