class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        for j in range(n):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
        ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
        ([0, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]),
    ]
    for nums, expected in test_cases:
        assert solution.moveZeroes(nums) == expected
