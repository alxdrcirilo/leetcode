class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1
        ops = 0

        while left < right:
            if nums[left] + nums[right] == k:
                ops += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                right -= 1
        return ops


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (([1, 2, 3, 4], 5), 2),
        (([3, 1, 3, 4, 3], 6), 1),
    ]
    for (nums, k), expected in test_cases:
        assert solution.maxOperations(nums, k) == expected
