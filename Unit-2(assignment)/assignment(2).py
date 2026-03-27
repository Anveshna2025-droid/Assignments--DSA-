# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Unit 2 Assignment: Data Structures Implementation & Analysis
# Submitted to = Deepak Kaushik Sir
# <==========================================================>

import ctypes

# 1. DYNAMIC ARRAY (Append with doubling resize + Pop)
class DynamicArray:
    def __init__(self):
        self.n = 0           # Actual elements
        self.capacity = 1    # Total slots
        self.A = self._make_array(self.capacity)

    def _make_array(self, cap):
        return (cap * ctypes.py_object)()

    def _resize(self, new_cap):
        """Amortized O(1) logic: Double capacity when full."""
        print(f"\n[RESIZE] Capacity reached {self.capacity}. Resizing to {new_cap}...")
        B = self._make_array(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

    def append(self, obj):
        if self.n == self.capacity:
            self._resize(2 * self.capacity)
        self.A[self.n] = obj
        self.n += 1
        print(f"Added {obj} | Size: {self.n}, Capacity: {self.capacity}")

    def pop(self):
        if self.n == 0:
            print("Underflow: Array is empty.")
            return None
        val = self.A[self.n - 1]
        self.A[self.n - 1] = None
        self.n -= 1
        return val

# 2. NODES & LINKED LIST STRUCTURES
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # Used for DLL

# 3. SINGLY LINKED LIST (SLL) OPERATIONS
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

# 4. DOUBLY LINKED LIST (DLL) EXTENSION
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_after_node(self, target_val, x):
        curr = self.head
        while curr and curr.data != target_val:
            curr = curr.next
        if curr:
            new_node = Node(x)
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node

# 5. STACK USING SLL (Top at Head)
class StackSLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top: return None
        data = self.top.data
        self.top = self.top.next
        return data

    def is_empty(self):
        return self.top is None

# 6. QUEUE USING SLL (O(1) with Tail Pointer)
class QueueSLL:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front: return None
        val = self.front.data
        self.front = self.front.next
        if not self.front: self.rear = None
        return val

# 7. WORKING PARENTHESES CHECKER
def is_balanced(expression):
    stack = StackSLL()
    pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()

# <==================== COMPLEXITY & AMORTIZED DISCUSSION ====================>
"""
1. DYNAMIC ARRAY ANALYSIS:
   - Append: Amortized O(1). While resizing takes O(n), it happens only after 
     capacity doubles, spreading the cost across many constant-time operations.
   - Pop: O(1) as it only involves pointer/index adjustment at the end.

2. LINKED LISTS (SLL/DLL):
   - Insertion at head: O(1).
   - Search/Delete by value: O(n) as it requires sequential traversal.
   - DLL Advantage: Bidirectional traversal and O(1) deletion if node is given.

3. STACK & QUEUE (SLL-BASED):
   - All operations (Push, Pop, Enqueue, Dequeue) are O(1) because they 
     manipulate only the Head or the Tail pointer.

4. PARENTHESES CHECKER:
   - Time Complexity: O(n) because we scan the input string exactly once.
   - Space Complexity: O(n) in the worst case (all opening brackets).
"""

if __name__ == "__main__":
    # Demo 1: Dynamic Array
    print("--- Dynamic Array Demo ---")
    da = DynamicArray()
    for i in range(5): da.append(i)

    # Demo 2: Parentheses Checker
    print("\n--- Parentheses Checker Demo ---")
    test_cases = ["{[()]}", "([)]", "(( ))"]
    for test in test_cases:
        print(f"'{test}' is balanced: {is_balanced(test)}")