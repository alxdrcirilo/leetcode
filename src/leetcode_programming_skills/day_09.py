class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        n = len(arr)
        diff = arr[1] - arr[0]

        for i in range(1, n - 1):
            if diff != arr[i + 1] - arr[i]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.canMakeArithmeticProgression([3, 5, 1])
    assert not solution.canMakeArithmeticProgression([1, 2, 4])
