class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            a, b = height[left], height[right]
            area = max(area, min(a, b) * (right - left))
            if a < b:
                left += 1
            else:
                right -= 1
        return area


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([1, 2, 4, 3], 4),
    ]
    for height, expected in test_cases:
        assert solution.maxArea(height) == expected
