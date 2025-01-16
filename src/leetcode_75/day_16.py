class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Edge case: #1
        # No 1's
        if sum(nums) == 0:
            return k if k < n else n

        # Edge case: #2
        # k is larger than the length of the nums array
        if k >= n:
            return n

        a = 0
        b = 0
        zeros = 0
        res = zeros

        while b < n - 1:
            # Find first range of consecutive digits (including 0's)
            while zeros < k and b < n - 1:
                if nums[b] == 0:
                    zeros += 1
                b += 1

            # Add trailing 1's
            while nums[b] == 1 and b < n - 1:
                b += 1

            # Include last digit
            if b == n - 1:
                if not (zeros == k and nums[b] == 0):
                    b += 1

            # Check if new range is maximum
            if (c := b - a) > res:
                res = c

            # Slide window to the right
            if zeros == k:
                zeros -= int(nums[a] == 0)
                a += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (([1,1,1,0,0,0,1,1,1,1,0], 2), 6),
        (([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), 10),
    ]
    for (nums, k), expected in test_cases:
        assert solution.longestOnes(nums, k) == expected