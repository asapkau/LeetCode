# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        #so i take mid as the root and then accordingly use the list put all the numbers lesser than that in left subtree and all greater than the root in right sub tree

        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])


        leftTree = nums[:mid]
        rightTree = nums[mid + 1 : len(nums)]

        root.left = self.sortedArrayToBST(leftTree)
        root.right = self.sortedArrayToBST(rightTree)

        return root



        