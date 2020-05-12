"""
// lc206-Reverse_Linked_List.py : Reverse a singly linked list.

// Example:
//    Input: 1->2->3->4->5->NULL
//    Output: 5->4->3->2->1->NULL

"""

def main():
    test_list_1 = create_test_list(1,2,3,4,5)
    print("Test list 1 is: {}".format(ListNode_to_str(test_list_1)))
    sln = Solution()
    result = sln.reverseList(test_list_1)
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
    def reverseList(self, head: ListNode) -> ListNode:
        itr = head
        prev = None
        while itr:
            next = itr.next
            itr.next = prev
            prev = itr
            itr = next
        return prev

if __name__ == '__main__':
    main()