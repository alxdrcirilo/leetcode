class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest, altitude = 0, 0
        for g in gain:
            highest = max(highest, (altitude := altitude + g))
        return highest


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    ]
    for gain, expected in test_cases:
        assert solution.largestAltitude(gain) == expected
