class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        return "".join(a + b for a, b in zip(word1, word2)) + (word1[n:] or word2[n:])


if __name__ == "__main__":
    solution = Solution()
    assert solution.mergeAlternately("abc", "def") == "adbecf"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
