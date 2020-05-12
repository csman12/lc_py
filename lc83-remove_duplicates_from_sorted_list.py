"""
lc83-remove_duplicates_from_sorted_list.py: Given a sorted linked list, delete all 
duplicates such that each element appears only once.

Example 1:
  Input: 1->1->2
  Output: 1->2

Example 2:
  Input: 1->1->2->3->3
  Output: 1->2->3
"""

def main():
    test_list = create_list([1, 1, 1, 2, 2, 2, 3, 3, 3, 3])
    print_list_node(test_list, "Starting Test List:")
    sln = Solution()
    test_list = sln.deleteDuplicates(test_list)
    print_list_node(test_list, "Final Test List:")

def create_list(values):
    if not values or len(values) < 1: return None
    head_node = ListNode(values[0])
    prev_node = head_node
    for i in range(1, len(values)):
        tmp_node = ListNode(values[i])
        prev_node.next = tmp_node
        prev_node = tmp_node
    return head_node

def print_list_node(node, bgn_str="List:"):
    print(bgn_str, end='')
    while node != None:
        print(node.val, end=' ')
        node = node.next
    print(" ")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        cur_node = head
        while cur_node.next != None:
            if cur_node.val == cur_node.next.val:
                next_next_node = cur_node.next.next
                cur_node.next.next = None
                cur_node.next = next_next_node
            else:
                cur_node = cur_node.next
        return head

if __name__ == "__main__": 
    main()