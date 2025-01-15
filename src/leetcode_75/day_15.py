class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}

        n = len(s)
        if n == 0:
            return 0
        elif n == k:
            return sum(c in vowels for c in s)

        a = s[0] in vowels
        b = sum(c in vowels for c in s[1:k])
        count = a + b
        res = count

        for i in range(1, len(s) - k + 1):
            count -= a
            count += s[i + k - 1] in vowels
            if count > res:
                res = count
            a = s[i] in vowels
        return res


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (("abciiidef", 3), 3),
        (("aeiou", 2), 2),
        (("leetcode", 3), 2),
    ]
    for (s, k), expected in test_cases:
        assert solution.maxVowels(s, k) == expected
