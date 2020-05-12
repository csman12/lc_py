"""
// lc19-Remove_Nth_Node_From_End_of_List.py
// Given a linked list, remove the n-th node from the end of list and return its head.

// Example:
//   Given linked list : 1->2->3->4->5, and n = 2.
//   After removing the second node from the end, the linked list becomes 1->2->3->5.

// Note: Given n will always be valid.
// Follow up: Could you do this in one pass ?
"""

def main():
    test_list_1 = create_test_list(1,2,3,4,5)
    print("Test list 1 is: {}".format(ListNode_to_str(test_list_1)))
    sln = Solution()
    result = sln.removeNthFromEnd(test_list_1, 0)
    print("Result list is: {}".format(ListNode_to_str(result)))

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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n < 1: return head
        cnt = 0
        itr = head
        n_itr = head
        while itr:
            if cnt < (n+1):
                cnt += 1
            else:
                n_itr = n_itr.next
            itr = itr.next
        
        if cnt == n: return head.next
        elif cnt < (n+1): return head

        if n_itr.next.next:
            n_itr.next = n_itr.next.next
        else:
            n_itr.next = None
        return head                

if __name__ == '__main__':
    main()