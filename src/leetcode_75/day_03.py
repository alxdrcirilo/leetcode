class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        return [i + extraCandies >= max_candies for i in candies]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 1, [True, False, True]),
    ]

    for candies, extraCandies, expected in test_cases:
        assert solution.kidsWithCandies(candies, extraCandies) == expected
