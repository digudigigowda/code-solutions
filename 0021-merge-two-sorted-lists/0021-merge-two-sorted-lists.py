# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Step 1: Convert ListNode objects into standard Python lists
        l, o = [], []
        while list1:
            l.append(list1.val)
            list1 = list1.next
        while list2:
            o.append(list2.val)
            list2 = list2.next

        # Step 2: YOUR EXACT LOGIC
        p = l + o
        sorted_p = sorted(p)

        # Step 3: Rebuild the ListNode structure for LeetCode
        dummy = current = ListNode(0)
        for val in sorted_p:
            current.next = ListNode(val)
            current = current.next

        return dummy.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna