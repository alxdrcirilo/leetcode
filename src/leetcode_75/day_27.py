class RecentCounter:
    def __init__(self):
        self.start = 0
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[self.start] < t - 3000:
            self.start += 1
        return len(self.requests) - self.start


if __name__ == "__main__":
    rc = RecentCounter()
    test_cases = [(1, 1), (100, 2), (3001, 3), (3002, 3)]
    for t, expected in test_cases:
        assert rc.ping(t) == expected
