class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        first = 2**31 - 1
        second = 2**31 - 1
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5], True),
        ([5, 4, 3, 2, 1], False),
        ([2, 1, 5, 0, 4, 6], True),
        ([20, 100, 10, 12, 5, 13], True),
        ([2, 4, -2, -3], False),
        ([1, 2, 1, 3], True),
        ([1, 5, 0, 4, 1, 3], True),
    ]
    for nums, expected in test_cases:
        assert solution.increasingTriplet(nums) == expected
