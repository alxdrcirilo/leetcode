from collections import deque


class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque(s)
        res = deque()
        while len(stack) > 0:
            if (i := stack.popleft()) != "*":
                res.append(i)
            else:
                res.pop()
        return "".join(res)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("leet**cod*e", "lecoe"),
        ("erase*****", ""),
    ]
    for s, expected in test_cases:
        assert solution.removeStars(s) == expected
