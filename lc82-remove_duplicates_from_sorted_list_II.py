"""
lc82-remove_duplicates_from_sorted_list_II.py: Given a sorted linked list, delete all 
nodes that have duplicate numbers, leaving only distinct numbers from the original list.
Return the linked list sorted as well.

Example 1:
  Input: 1->2->3->3->4->4->5
  Output: 1->2->5

Example 2:
  Input: 1->1->1->2->3
  Output: 2->3
"""

def main():
    test_list = create_list([1, 1, 2])
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
    if node == None: 
        print(bgn_str)
        return
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
        rtn_head = head
        prev_node = None
        cur_node = head
        while cur_node != None:
            if prev_node == None and cur_node.next != None and cur_node.next.val == cur_node.val:
                val_to_delete = cur_node.val
                while cur_node != None and cur_node.val == val_to_delete:
                    next_node = cur_node.next
                    cur_node.next = None
                    cur_node = next_node
                    rtn_head = cur_node
            elif cur_node.next != None and cur_node.val == cur_node.next.val:
                val_to_delete = cur_node.val
                while cur_node != None and cur_node.val == val_to_delete:
                    next_node = cur_node.next
                    cur_node.next = None
                    cur_node = next_node
                prev_node.next = cur_node
            else:
                prev_node = cur_node
                cur_node = cur_node.next
            
        return rtn_head


if __name__ == "__main__":
    main()