class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change = {5: 0, 10: 0}

        for i in bills:
            if i == 5:
                change[5] += 1
                continue

            elif i == 10:
                if change[5] > 0:
                    change[5] -= 1
                    change[10] += 1
                    continue
                return False

            elif i == 20:
                if change[10] > 0 and change[5] > 0:
                    change[10] -= 1
                    change[5] -= 1
                    continue
                elif change[5] >= 3:
                    change[5] -= 3
                    continue
                return False

        return True


if __name__ == "__main__":
    solution = Solution()
    assert solution.lemonadeChange([5, 5, 5, 10, 20]) is True
    assert solution.lemonadeChange([5, 5, 10, 10, 20]) is False
