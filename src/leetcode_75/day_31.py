# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr is not None:
            following = curr.next
            curr.next = prev
            prev = curr
            curr = following

        return prev


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1))))),
        ),
    ]
    for head, expected in test_cases:
        assert solution.reverseList(head) == expected
