"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root  # The LCA

        return left if left else right

    def main(self):
        n3 = TreeNode(3)
        n5 = TreeNode(5)
        n1 = TreeNode(1)
        n6 = TreeNode(6)
        n2 = TreeNode(2)
        n0 = TreeNode(0)
        n8 = TreeNode(8)
        n7 = TreeNode(7)
        n4 = TreeNode(4)

        n3.left = n5;
        n3.right = n1
        n5.left = n6;
        n5.right = n2
        n1.left = n0;
        n1.right = n8
        n2.left = n7;
        n2.right = n4

        # Example 1: LCA of 5 and 1 is 3
        result1 = self.lowestCommonAncestor(n3, n5, n1)
        print("LCA of 5 and 1:", result1.val)

        # Example 2: LCA of 5 and 4 is 5
        result2 = self.lowestCommonAncestor(n3, n5, n4)
        print("LCA of 5 and 4:", result2.val)

        # Example 3: LCA of 1 and 2 is 3
        result3 = self.lowestCommonAncestor(n3, n1, n2)
        print("LCA of 1 and 2:", result3.val)


if __name__ == "__main__":
    sol = Solution()
    sol.main()
