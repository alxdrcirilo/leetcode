class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


if __name__ == "__main__":
    solution = Solution()
    assert solution.toLowerCase("Hello") == "hello"
    assert solution.toLowerCase("here") == "here"
    assert solution.toLowerCase("LOVELY") == "lovely"
