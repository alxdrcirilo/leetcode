class Solution:
    def average(self, salary: list[int]) -> float:
        minimum = maximum = salary[0]
        salary_sum = 0
        for i in salary:
            if i < minimum:
                minimum = i
            elif i > maximum:
                maximum = i
            salary_sum += i
        return (salary_sum - minimum - maximum) / (len(salary) - 2)


if __name__ == "__main__":
    solution = Solution()
    assert solution.average([4000, 3000, 1000, 2000]) == 2500.00000
    assert solution.average([1000, 2000, 3000]) == 200
