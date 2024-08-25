#User function Template for python3

from collections import deque, defaultdict

class Solution:
    def minTime(self, root, target):
        # Step 1: Create a map to store the parent reference for each node
        parent_map = {}
        self.createParentMap(root, parent_map)
        
        # Step 2: Perform BFS starting from the target node
        return self.burnTree(root, target, parent_map)
    
    def createParentMap(self, node, parent_map, parent=None):
        if not node:
            return
        
        if parent:
            parent_map[node] = parent
        
        self.createParentMap(node.left, parent_map, node)
        self.createParentMap(node.right, parent_map, node)
    
    def burnTree(self, root, target, parent_map):
        # Step 2.1: Find the target node in the tree
        target_node = self.findTarget(root, target)
        
        # Step 2.2: Start BFS from the target node
        queue = deque([target_node])
        visited = set([target_node])
        time = 0
        
        while queue:
            level_size = len(queue)
            burn_happened = False
            
            for _ in range(level_size):
                node = queue.popleft()
                
                # Process the left child
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                    burn_happened = True
                
                # Process the right child
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)
                    burn_happened = True
                
                # Process the parent
                if node in parent_map and parent_map[node] not in visited:
                    queue.append(parent_map[node])
                    visited.add(parent_map[node])
                    burn_happened = True
            
            # Increase time if at least one node was burned in this round
            if burn_happened:
                time += 1
        
        return time
    
    def findTarget(self, node, target):
        # Helper function to find the target node
        if not node:
            return None
        if node.data == target:
            return node
        
        left_search = self.findTarget(node.left, target)
        if left_search:
            return left_search
        
        return self.findTarget(node.right, target)