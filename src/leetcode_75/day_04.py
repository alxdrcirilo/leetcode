from math import ceil, floor


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowers = sum(flowerbed)
        planted = [i for i, x in enumerate(flowerbed) if x == 1]
        length = len(flowerbed)

        if flowers:
            # Case: #1
            # Get plots before first and after last planted
            first = floor(planted[0] / 2)
            last = floor((length - planted[-1] - 1) / 2)
            available = sum(
                [ceil((b - a - 3) / 2) for a, b in zip(planted[:-1], planted[1:])]
            )
            return flowers + n <= flowers + available + first + last
        else:
            # Case: #2
            # Empty flowerbed
            return flowers + n <= ceil(length / 2)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([1, 0, 0, 0, 1], 1, True),
        ([1, 0, 0, 0, 1], 2, False),
        ([0, 0, 1, 0, 0], 2, True),
        ([0, 0, 0, 0, 0], 3, True),
        ([1, 0, 0, 0, 0, 1], 2, False),
        ([1, 0, 0, 0, 0, 0, 1], 2, True),
        ([1, 0, 0, 0, 0, 0, 0, 0, 1], 3, True),
    ]

    for flowerbed, n, expected in test_cases:
        assert solution.canPlaceFlowers(flowerbed, n) == expected
