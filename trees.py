#1
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr=root
        
        while curr is not None:
            if curr.val==val:
                return curr
            elif (curr.val > val):
                curr= curr.left
            else:
                curr = curr.right

        return None



#2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        q=deque([root1])
        q2=deque([root2])
        seq1=[]
        seq2=[]
        while q:
            curr=q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            if (curr.left is None) and (curr.right is None):
                seq1.append(curr.val)
        
        while q2:
            curr=q2.popleft()
            if curr.left:
                q2.append(curr.left)
            if curr.right:
                q2.append(curr.right)
            if (curr.left is None) and (curr.right is None):
                seq2.append(curr.val)
        print(seq1, seq2)
        return seq1 == seq2



#3
class Solution(object):
    def leafSimilar(self, root1, root2):
        def leaf_seq(root, seq):
            if not root:
                return
            if  not root.left and not root.right:
                seq.append(root.val)
            leaf_seq(root.left, seq)
            leaf_seq(root.right, seq)

        seq1=[]
        seq2=[]

        leaf_seq(root1, seq1)
        leaf_seq(root2, seq2)

        return seq1==seq2

        