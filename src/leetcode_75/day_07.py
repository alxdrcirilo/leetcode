class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        # Product on left
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Product on right
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ]

    for nums, expected in test_cases:
        assert solution.productExceptSelf(nums) == expected
