#https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        
        que = []
        que.append(root)
        que.append(2000)
        r_list = []
        temp = []
        while(len(que)!=0):
            value = que[0]
            que.pop(0)
            if value==2000:
                if len(que)==0:
                    r_list.append(temp)
                    break
                r_list.append(temp)
                temp = []
                que.append(2000)
                
            else:
                temp.append(value.val)
                if value.left!=None:
                    que.append(value.left)
                if value.right!=None:
                    que.append(value.right)
        return r_list
            
        
