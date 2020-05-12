"""
  lc590-n-ary_tree_postorder_traversal.py: Given an n-ary tree, 
  return the postorder traversal of its nodes' values.
  Nary-Tree input serialization is represented in their level 
  order traversal, each group of children is separated by the 
  null value (See examples).

  Constraints:
  The height of the n-ary tree is less than or equal to 1000
  The total number of nodes is between [0, 10^4]

  Follow up:
  Recursive solution is trivial, could you do it iteratively?

  Example 1:
  Input: root = [1,null,3,2,4,null,5,6]
  Output: [5,6,3,2,4,1]

  Example 2:
  Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
  Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""
import queue

def main():
    null = None
    tree_list = []  
    root = create_tree(tree_list)
    sln = Solution()
    po_list_1 = sln.postorder_recursion(root)
    print("Post Order Traversal List 1:", po_list_1)
    po_list_2 = sln.postorder(root)
    print("Post Order Traversal List 2:", po_list_2)

def create_tree(tree_list):
    # split list into a list of lists using delimiter of None
    if not tree_list: return None
    child_lists = []
    child_list = []
    for val in tree_list:
        if val != None:
            child_list.append(val)
        else:
            child_lists.append(child_list)
            child_list = []
    child_lists.append(child_list)

    # perform a level order like traversal using a queue
    # during traversal link the child nodes to their parent nodes
    myQ = queue.Queue()
    root = Node(val=tree_list[0], children=None)
    myQ.put(root)
    child_lists_i = 1
    while not myQ.empty():
        parent_node = myQ.get()
        if child_lists_i >= len(child_lists):
            parent_node.children = None
        else:
            link_child_nodes(parent_node, child_lists[child_lists_i])
        if parent_node.children:
            for node in parent_node.children:
                myQ.put(node)
        child_lists_i += 1
    return root

def link_child_nodes(parent_node, child_list):
    if not child_list: 
        parent_node.children = None
        return
    children = []
    for child in child_list: 
        children.append(Node(child, None))
    parent_node.children = children

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> list:
        if not root: return root
        post_order_list = []
        po_stack = []
        level_stack = []
        level_stack.append([root])
        while len(level_stack):
            if len(level_stack):
                level_list = level_stack[len(level_stack)-1] # get last child list on stack
                
            if level_list:
                next_node = level_list.pop()
                po_stack.append(next_node)
                if next_node.children:
                    level_stack.append([x for x in reversed(next_node.children)])
                else:
                    level_stack.append(None)
                continue
            else:
                level_stack.pop() 
                if len(po_stack):
                    cur_node = po_stack.pop()
                    post_order_list.append(cur_node.val)

        return post_order_list
    
    # recusion form of post order traversal
    def postorder_recursion(self, root: 'Node') -> list:
        if not root: return root
        postorder_list = []
        for i in range(len(root.children)):
            self._postorder_recursion(root.children[i], postorder_list)
        postorder_list.append(root.val)   
        return postorder_list

    def _postorder_recursion(self, node=None, post_order_list=[]):
        if node == None: return
        if node.children != None:
            for i in range(len(node.children)): 
                self._postorder_recursion(node.children[i], post_order_list)
        post_order_list.append(node.val)

if __name__ == "__main__": main()