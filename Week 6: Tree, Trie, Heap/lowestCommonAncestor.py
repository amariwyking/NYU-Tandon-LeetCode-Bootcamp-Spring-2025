class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # looking for the deepest node that's a parent to both target nodes
        
        # rephrased:
        # we need the node with the greatest depth, whose subtrees contain both target nodes
        
        # we should be able to perform this recursively, such that we keep calling lowestCommonAncestor on each child node
            
        # when dealing with recursion, we expect the parameters passed to the function to trigger the failure case
        
        # for example, if we make our recursive call on the left subtree and that subtree happens to be empty, this situation should be the first thing addressed when the function executes
        
        # There are two cases which indicate we should look no further
        # Either:
        #   - The tree is empty
        #   - The root node matches one of the targets
        if root == None or root == p or root == q:
            return root
        
        # If the root node doesn't trigger a return statement, we must then explore the subtrees of the current root
        
        
        left_result = self.lowestCommonAncestor(root.left, p, q)
        right_result = self.lowestCommonAncestor(root.right, p, q)
        
        # if either subtree returns something not null, then the LCA is the current node
            # that is because once we go step down to the next level, only one of the targets could be in the subtree
        
        # if there is a target in both subtrees, the current root is the LCA
        if left_result and right_result:
            return root
        
        return left_result if left_result else right_result
        
        pass