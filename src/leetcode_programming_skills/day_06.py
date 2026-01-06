class Solution:
    def moveZeroes(self, nums: list[int]) -> list[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        slow = 0
        for fast in range(n):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums


if __name__ == "__main__":
    solution = Solution()
    assert solution.moveZeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert solution.moveZeroes([0]) == [0]
