class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d: dict = {}
        for i in arr:
            if d.get(i) is None:
                d[i] = 1
            else:
                d[i] += 1
        return len(set(d.values())) == len(d.keys())


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ]
    for arr, expected in test_cases:
        assert solution.uniqueOccurrences(arr) == expected
