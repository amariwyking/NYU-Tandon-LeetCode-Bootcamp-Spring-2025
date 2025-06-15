from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def RightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We want to imagine that we are looking at the tree from the right side
        # This means, our view will be the rightmost node on each level of the tree
        
        if not root:
            return []    
        
        # Initialize list of rightmost node at each tree level
        result = []
        
        # Initialize a queue which keeps track of nodes to be explored and their level
        queue = [((root, 0))]
        
        # while there's a node to be explored on this level
        while queue:
            (node, level) = deque(queue)
            
            # If the current level is greater than the result we are exploring a new level
            if level > len(result):
                result.append(node.value)
                
            # process all the nodes at this level
            while queue and queue[0][1] == level:
                queue.append(queue)
            
        return result
    
        """
        
        result.len = 0
        
        
        
        """