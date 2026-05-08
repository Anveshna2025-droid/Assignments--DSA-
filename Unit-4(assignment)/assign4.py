# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Unit 4 Assignment: Non-Linear Data Structures & Hashing
# Submitted to = Deepak Kaushik Sir
# <==========================================================>

from collections import deque

# 1. BINARY SEARCH TREE (BST) IMPLEMENTATION
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return BSTNode(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key):
        curr = self.root
        while curr:
            if curr.key == key: return True
            curr = curr.left if key < curr.key else curr.right
        return False

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

# 2. GRAPH ADJACENCY LIST & NETWORK TRAVERSALS
class NetworkGraph:
    def __init__(self):
        self.adj_list = {}

    def add_connection(self, u, v):
        if u not in self.adj_list: self.adj_list[u] = []
        if v not in self.adj_list: self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def breadth_first_search(self, start):
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def depth_first_search(self, start, visited=None):
        if visited is None: visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.adj_list.get(start, []):
            if neighbor not in visited:
                self.depth_first_search(neighbor, visited)

# 3. HASH TABLE WITH SEPARATE CHAINING
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _generate_hash(self, key):
        return sum(ord(c) for c in str(key)) % self.size

    def put(self, key, value):
        index = self._generate_hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._generate_hash(key)
        for item in self.table[index]:
            if item[0] == key: return item[1]
        return None

# <==================== SYSTEM ANALYSIS & OBSERVATIONS ====================>
"""
1. HIERARCHICAL DATA (BST):
   - The BST provides an average time complexity of O(log n) for operations.
   - It is utilized for maintaining naturally ordered datasets.

2. NETWORK DATA (Graphs):
   - BFS is implemented to find shortest paths in unweighted networks.
   - DFS is implemented for deep exploration and connectivity analysis.

3. DATA MAPPING (Hashing):
   - Separate Chaining effectively manages collisions by maintaining 
     linked lists (buckets) at each hash index, ensuring data integrity.
"""

if __name__ == "__main__":
    # BST Demonstration
    print("--- Binary Search Tree Output ---")
    tree = BinarySearchTree()
    for x in [40, 20, 60, 10, 30, 50, 70]: tree.insert(x)
    print("In-order (Sorted):", end=" ")
    tree.inorder_traversal(tree.root)
    
    # Graph Demonstration
    print("\n\n--- Graph Traversal Output ---")
    net = NetworkGraph()
    for u, v in [('A','B'), ('A','C'), ('B','D'), ('C','E')]: net.add_connection(u, v)
    print("BFS Path from A:", net.breadth_first_search('A'))
    print("DFS Path from A:", end=" ")
    net.depth_first_search('A')
    
    # Hashing Demonstration
    print("\n\n--- Hash Table Verification ---")
    storage = HashTable(5)
    storage.put("ID_101", "Anveshna")
    storage.put("ID_102", "Data_Point_B")
    print(f"Retrieving ID_101: {storage.get('ID_101')}")