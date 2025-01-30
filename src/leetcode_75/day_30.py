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
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even  # Keep track of the start of the even list

        while even and even.next:
            odd.next = even.next  # Link odd nodes
            odd = odd.next
            even.next = odd.next  # Link even nodes
            even = even.next

        # Append the even list to the end of the odd list
        odd.next = even_head
        return head


if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            ListNode(1, ListNode(3, ListNode(5, ListNode(2, ListNode(4))))),
        ),
    ]
    for head, expected in test_cases:
        assert solution.oddEvenList(head) == expected
