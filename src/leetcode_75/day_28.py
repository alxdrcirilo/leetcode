class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        radiant = [i for i in range(n) if senate[i] == "R"]
        dire = [i for i in range(n) if senate[i] == "D"]

        while radiant and dire:
            r_idx = radiant.pop(0)
            d_idx = dire.pop(0)
            if r_idx < d_idx:
                radiant.append(r_idx + n)
            else:
                dire.append(d_idx + n)
        
        return "Radiant" if radiant else "Dire"

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("RD", "Radiant"),
        ("RDD", "Dire"),
    ]
    for senate, expected in test_cases:
        assert solution.predictPartyVictory(senate) == expected
