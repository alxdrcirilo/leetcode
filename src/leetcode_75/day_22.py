from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        if set(word1) != set(word2):
            return False

        freq1 = Counter(word1)
        freq2 = Counter(word2)

        return sorted(freq1.values()) == sorted(freq2.values())


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (("abc", "bca"), True),
        (("a", "aa"), False),
        (("cabbba", "abbccc"), True),
    ]
    for (word1, word2), expected in test_cases:
        assert solution.closeStrings(word1, word2) == expected
