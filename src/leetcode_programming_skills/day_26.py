class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        if len(coordinates) == 2:
            return True

        n = len(coordinates)
        (x0, y0), (x1, y1) = coordinates[:2]
        for i in range(1, n):
            x2, y2 = coordinates[i]
            if (y2 - y1) * (x1 - x0) != (y1 - y0) * (x2 - x1):
                return False
        return True


if __name__ == "__main__":
    solution = Solution()
    assert (
        solution.checkStraightLine(
            [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
        )
        is True
    )
    assert (
        solution.checkStraightLine(
            [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
        )
        is False
    )
    assert (solution.checkStraightLine([[1, 2], [2, 3], [3, 5]])) is False
