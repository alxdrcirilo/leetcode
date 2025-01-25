class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res: list = []

        for a in asteroids:
            while res and a < 0 < res[-1]:
                if a + res[-1] < 0:
                    res.pop()
                elif a + res[-1] > 0:
                    break
                else:
                    res.pop()
                    break
            else:
                res.append(a)

        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
    ]
    for asteroids, expected in test_cases:
        assert solution.asteroidCollision(asteroids) == expected
