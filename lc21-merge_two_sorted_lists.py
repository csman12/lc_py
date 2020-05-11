"""
// lc21-merge_two_sorted_lists.py : Merge two sorted linked lists and return it as a new list. 
// The new list should be made by splicing together the nodes of the first two lists.

// Example:
//     Input: 1->2->4, 1->3->4
//     Output: 1->1->2->3->4->4
"""
def main():
    test_list_1 = create_test_list(1,3,5)
    test_list_2 = create_test_list(2,4,6)
    print("Test list 1 is: {}".format(ListNode_to_str(test_list_1)))
    print("Test list 2 is: {}".format(ListNode_to_str(test_list_2)))

    merged_list = Solution.mergeTwoLists(Solution(), test_list_1, test_list_2)
    print("Merged list is: {}".format(ListNode_to_str(merged_list)))

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_test_list(*args):
    if args is None: return None
    head = ListNode(args[0])
    itr = head
    for i in range(1, len(args)):
        itr.next = ListNode(args[i])
        itr=itr.next
    return head

def ListNode_to_str(l: ListNode):
    num_list = []
    itr = l
    while itr is not None:
        num_list.append(str(itr.val))
        itr = itr.next
    return " ".join(num_list)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        slnList = ListNode(0)
        itr = slnList
        while l1 or l2:
            if (l1 and l2 and l1.val < l2.val) or (not l2):
                itr.next = l1
                l1 = l1.next
            else:
                itr.next = l2
                l2 = l2.next
            itr = itr.next
        return slnList.next

if __name__ == '__main__':
    main()