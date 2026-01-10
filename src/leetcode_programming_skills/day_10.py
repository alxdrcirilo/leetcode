class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        inc = dec = False
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                inc = True
            elif nums[i - 1] > nums[i]:
                dec = True
            if inc and dec:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.isMonotonic([1, 2, 2, 3])
    assert solution.isMonotonic([6, 5, 4, 4])
    assert not solution.isMonotonic([1, 3, 2])
    assert solution.isMonotonic([9])
