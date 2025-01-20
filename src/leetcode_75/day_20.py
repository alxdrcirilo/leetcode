class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2), list(set2 - set1)]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (([1, 2, 3], [2, 4, 6]), [[1, 3], [4, 6]]),
        (([1, 2, 3, 3], [1, 1, 2, 2]), [[3], []]),
    ]
    for (nums1, nums2), expected in test_cases:
        assert solution.findDifference(nums1, nums2) == expected
