class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)


if __name__ == "__main__":
    solution = Solution()
    assert solution.myPow(2.00000, 10) == 1024.00000
    assert solution.myPow(2.00000, -2) == 0.25000
