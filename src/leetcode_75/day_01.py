class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_chars = min(len(word1), len(word2))
        remainder = max(word1, word2, key=len)[min_chars:]
        result = [word1[i] + word2[i] for i in range(min_chars)]
        return "".join(result) + remainder


if __name__ == "__main__":
    solution = Solution()
    assert solution.mergeAlternately("abc", "pqr") == "apbqcr"
    assert solution.mergeAlternately("ab", "pqrs") == "apbqrs"
    assert solution.mergeAlternately("abcd", "pq") == "apbqcd"
