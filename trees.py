# 50, 30, 70, 60, 80, 65
from typing import Optional,Any, Tuple
from collections import deque
class BSTNode:
    def __init__(self, number: int) -> None:
        self.number = number
        self.left_pointer: BSTNode | None = None
        self.right_pointer:BSTNode | None = None

    # BST operations
    def insert_node(self, number):
        if number > self.number:
            if self.right_pointer is None:
                self.right_pointer = BSTNode(number=number)
            else:
                self.right_pointer.insert_node(number=number)
        elif number < self.number:
            if self.left_pointer is None:
                self.left_pointer = BSTNode(number=number)
            else:
                self.left_pointer.insert_node(number=number)

    def search_node(self, number) -> Any:
        if self.number == number:
            print(f"--The number {number} is found. --")
            return self.number
        if (number > self.number and self.right_pointer is None) or (number < self.number and self.left_pointer is None):
            print(f"--The number {number} is not available--")
            return
        if number > self.number and self.right_pointer is not None:
            return self.right_pointer.search_node(number=number)
        if number < self.number and self.left_pointer is not None:
            return self.left_pointer.search_node(number=number)

    def delete_node(self, number) -> Any:
        if self.number > number:
            if self.left_pointer is not None:
                self.left_pointer = self.left_pointer.delete_node(number=number)
            return self
        elif number < self.number:
            if self.right_pointer is not None:
                self.right_pointer = self.right_pointer.delete_node(number=number)
            return self
        
        if self.left_pointer is None and self.right_pointer is None:
            return None

        if self.left_pointer is None:
            return self.right_pointer
        if self.right_pointer is None:
            return self.left_pointer
        
        successor = self.right_pointer
        while successor.left_pointer:
            successor = successor.left_pointer
        
        self.number = successor.number
        
        self.right_pointer = self.right_pointer.delete_node(successor.number)
        
        return self


            

    # BST Traversals
    def pre_order_traversal(self):
        print(f"--{self.number}--")
        if self.left_pointer is not None:
            self.left_pointer.pre_order_traversal()
        if self.right_pointer is not None:
            self.right_pointer.pre_order_traversal()

    def in_order_traversal(self):
        if self.left_pointer is not None:
            self.left_pointer.in_order_traversal()
        print(f"--{self.number}--")
        if self.right_pointer is not None:
            self.right_pointer.in_order_traversal()  

    def post_order_traversal(self):
        if self.left_pointer is not None:
            self.left_pointer.post_order_traversal()
        if self.right_pointer is not None:
            self.right_pointer.post_order_traversal()  
        print(f"--{self.number}--")

    # Since this is BFS, it is done by queue
    def level_order_traversal(self):
        queue = deque()
        queue.append(self)
        while queue:
            popped = queue.popleft()
            print(popped.number)
            if popped.left_pointer is not None:
                queue.append(popped.left_pointer)
            if popped.right_pointer is not None:
                queue.append(popped.right_pointer)

    # Utilities
    def get_height(self) -> int:
        left_height =  self.left_pointer.get_height() if self.left_pointer else 0
        right_height = self.right_pointer.get_height()if self.right_pointer else 0      
        return 1 + max(left_height, right_height)

    def count_nodes(self) -> int:
        left = self.left_pointer.count_nodes() if self.left_pointer else 0
        right  = self.right_pointer.count_nodes() if self.right_pointer else 0
        return 1 + left + right
    
    def count_leaf_nodes(self) -> int:
        if self.left_pointer is None and self.right_pointer is None:
            return 1
        left = self.left_pointer.count_leaf_nodes() if self.left_pointer else 0
        right = self.right_pointer.count_leaf_nodes() if self.right_pointer else 0
        return left + right

    def find_min(self) -> int:
        if self.left_pointer is None:
            return self.number
        return self.left_pointer.find_min()

    def find_max(self) -> int:
        if self.right_pointer is None:
            return self.number
        return self.right_pointer.find_max()

    def lowest_common_ancestor(self, node1, node2) -> Any:
        if (node1 >= self.number and node2 <= self.number ) or ( node1 <= self.number and node2 >= self.number):
            return self.number
        else:
            if node1 > self.number and node2 > self.number:
                if self.right_pointer is None:
                   return "The point don't exist at all. " 
                return self.right_pointer.lowest_common_ancestor(node1=node1, node2=node2)
                
            if node1 < self.number and node2 < self.number:
                if self.left_pointer is None:
                    return "The point don't exists at all. "
                return self.left_pointer.lowest_common_ancestor(node1=node1, node2=node2)

    def is_balanced(self) -> Tuple[int, bool]:
        left_height, left_balanced = self.left_pointer.is_balanced() if self.left_pointer else (0, True)
        right_height, right_balanced = self.right_pointer.is_balanced() if self.right_pointer else (0, True)
        balanced = abs(left_height - right_height) <= 1 and left_balanced and right_balanced
        return (1 + max(left_height, right_height), balanced)

    def diameter(self):
        pass

    def path_sum(self, target: int):
        pass

    def serialize(self):
        pass

    def deserialize(self, data: int):
        pass

bst_root = BSTNode(10)
bst_root.insert_node(12)
bst_root.insert_node(5)
bst_root.insert_node(3)
bst_root.insert_node(7)
bst_root.insert_node(15)
bst_root.insert_node(13)
bst_root.insert_node(17)
# print(bst_root.get_height())
print(bst_root.lowest_common_ancestor(6,7))


from typing import Optional, Any, Tuple

# get_height → update_height → get_balance_factor → rotations → insert_node → delete_node

class AVLNode:
    def __init__(self, number: int) -> None:
        """
        Initialize an AVL tree node.
        """
        self.number: int = number
        self.left_pointer: Optional["AVLNode"] = None
        self.right_pointer: Optional["AVLNode"] = None
        self.height: int = 1  # Each node tracks its height for balance factor

    # ---------------- AVL Utility Functions ----------------
    def get_height(self) -> Any:
        """
        Returns the height of the node.
        """
        left = self.left_pointer.get_height() if self.left_pointer else 0
        right = self.right_pointer.get_height() if self.right_pointer else 0
        return 1 + max(left, right)
        

    def get_balance_factor(self) -> int:
        """
        Returns balance factor = height(left) - height(right)
        """
        left = self.left_pointer.get_height() if self.left_pointer else 0
        right = self.right_pointer.get_height() if self.right_pointer else 0
        return left-right

    def update_height(self) -> None:
        """
        Updates the node's height based on children heights.
        """
        pass

    # ---------------- Rotations ----------------
    def left_rotate(self) -> "AVLNode":
        """
        Performs left rotation and returns new root of the subtree.
        """
        pass

    def right_rotate(self) -> "AVLNode":
        """
        Performs right rotation and returns new root of the subtree.
        """
        pass

#     If you're interested, there is also a very powerful implementation trick that reduces AVL logic to only two rotation functions (left rotation and right rotation), and the four cases become trivial.

# Most clean AVL implementations use that approach

    # ---------------- AVL Operations ----------------
    # AVL insert must always return the root of the current subtree,
    def insert_node(self, number: int) -> Any:
        if number > self.number:
            if self.right_pointer is None:
                self.right_pointer = AVLNode(number=number)
            else:
                self.right_pointer = self.right_pointer.insert_node(number=number)
                 
        elif number < self.number:
            if self.left_pointer is None:
                self.left_pointer = AVLNode(number=number)
            else:
                self.left_pointer = self.left_pointer.insert_node(number=number)
        
        self.height = 1 + max(self.helper_to_calculate_height(self.left_pointer), self.helper_to_calculate_height(self.right_pointer))
        balance_factor = self.helper_to_calculate_height(self.left_pointer) - self.helper_to_calculate_height(self.right_pointer)

        # for balancing there are always three cases, that is it. 
        # We calculate unbalanced node(which is root of a subtree) and the node that made is unbalalnced
        # While we may think that it can be of any ehight, there actually isn't
        # The height is mostly of 3 that is it. and with common sense, we can know that it has 4 cases
        
        
        left_subtree_of_left_child = True if balance_factor > 1 and self.left_pointer is not None and number < self.left_pointer.number else False
        right_subtree_of_left_child = True if balance_factor > 1 and self.left_pointer is not None and number > self.left_pointer.number else False

        left_subtree_of_right_child = True if balance_factor < -1 and self.right_pointer is not None and number < self.right_pointer.number else False
        right_subtree_of_right_child = True if balance_factor < -1 and self.right_pointer is not None and number > self.right_pointer.number else False

        # if balance_factor < -1: # right heavy
        #     pass
        # elif balance_factor > 1: # Left heavy
        #     pass

        if left_subtree_of_left_child:
            top = self
            assert self.left_pointer is not None
            top.left_pointer= self.left_pointer.right_pointer
            # right rotation
            to_be_returned: AVLNode = self.left_pointer
            to_be_returned.right_pointer = top
            # you can see here it is 4 functioon calls, we can do it to 3 calls by optimization
            top.height = 1 + max(self.helper_to_calculate_height(top.left_pointer), self.helper_to_calculate_height(top.right_pointer))
            to_be_returned.height = 1 + max(self.helper_to_calculate_height(to_be_returned.left_pointer), to_be_returned.helper_to_calculate_height(to_be_returned.right_pointer))
            
            # copied from chatgpt 
            # left_h = self.helper_to_calculate_height(top.left_pointer)
            # right_h = self.helper_to_calculate_height(top.right_pointer)
            # top.height = 1 + max(left_h, right_h)

            # # now update height of new_root
            # left_h = self.helper_to_calculate_height(new_root.left_pointer)
            # right_h = top.height   # ← reuse, no helper call needed
            # new_root.height = 1 + max(left_h, right_h)


            return to_be_returned

        if right_subtree_of_left_child:
            top = self
            assert top.left_pointer is not None
            to_be_rotated = top.left_pointer
            node = to_be_rotated.right_pointer
            assert node is not None
            T2 = node.left_pointer
            T3 = node.right_pointer

            top.left_pointer = node

            assert top.left_pointer is not None
            top.left_pointer.left_pointer = to_be_rotated
            # assert top.right_pointer is not None
            # top.right_pointer.left_pointer = T3

            ## Same as LL now
            to_be_returned: AVLNode = top.left_pointer
            to_be_returned.right_pointer = top
            assert to_be_returned.left_pointer is not None
            to_be_returned.left_pointer.right_pointer = T2
            to_be_returned.right_pointer.left_pointer = T3

            top.height = 1 + max(self.helper_to_calculate_height(top.left_pointer), self.helper_to_calculate_height(top.right_pointer) )
            to_be_returned.height = 1 + max(self.helper_to_calculate_height(to_be_returned.left_pointer), self.helper_to_calculate_height(to_be_returned.right_pointer))

            return to_be_returned

        if right_subtree_of_right_child:
            top = self
            assert self.right_pointer is not None
            T2 = self.right_pointer.left_pointer
            to_be_returned: AVLNode = self.right_pointer
            to_be_returned.left_pointer = top
            to_be_returned.left_pointer.right_pointer = T2

            top.height = 1 + max(self.helper_to_calculate_height(top.left_pointer), self.helper_to_calculate_height(top.right_pointer))
            to_be_returned.height = 1 + max(self.helper_to_calculate_height(to_be_returned.left_pointer), self.helper_to_calculate_height(to_be_returned.right_pointer))

            return to_be_returned

        if left_subtree_of_right_child:
            
            assert self.right_pointer is not None
            assert self.right_pointer.left_pointer is not None
            T3 = self.right_pointer.left_pointer.right_pointer

            right_point = self.right_pointer
            node = right_point.left_pointer
            assert node is not None
            node.right_pointer = right_point
            self.right_pointer = node

            assert self.right_pointer is not None
            assert self.right_pointer.right_pointer is not None
            self.right_pointer.right_pointer.left_pointer = T3
            
            # self is still that. so
            top = self
            assert top.right_pointer is not None
            to_be_returned: AVLNode = top.right_pointer
            to_be_moved_t2 = to_be_returned.left_pointer
            to_be_returned.left_pointer = top
            to_be_returned.left_pointer.right_pointer = to_be_moved_t2

            top.height = 1 + max(self.helper_to_calculate_height(self.left_pointer), self.helper_to_calculate_height(self.right_pointer))
            to_be_returned.height = 1 = max(self.helper_to_calculate_height(to_be_returned.left_pointer), self.helper_to_calculate_height(to_be_returned.right_pointer))

            return to_be_returned

            
             

        return self

    def helper_to_calculate_height(self, node):
        if node is None:
            return 0
        return node.height
                

    def delete_node(self, number: int) -> Optional["AVLNode"]:
        """
        Deletes a node and rebalances the tree.
        Returns the new root of the subtree.
        """
        pass

    def search_node(self, number: int) -> Optional["AVLNode"]:
        """
        Searches for a node with the given number.
        Returns the node if found, else None.
        """
        pass

    # ---------------- Traversals ----------------
    def in_order_traversal(self) -> None:
        """
        Prints or collects nodes in in-order sequence.
        """
        pass

    def pre_order_traversal(self) -> None:
        """
        Prints or collects nodes in pre-order sequence.
        """
        pass

    def post_order_traversal(self) -> None:
        """
        Prints or collects nodes in post-order sequence.
        """
        pass

    def level_order_traversal(self) -> None:
        """
        Prints or collects nodes level by level (BFS).
        """
        pass

    # ---------------- Extra Utilities ----------------
    def find_min(self) -> "AVLNode":
        """
        Finds node with minimum value in the subtree.
        """
        pass

    def find_max(self) -> "AVLNode":
        """
        Finds node with maximum value in the subtree.
        """
        pass

    def count_nodes(self) -> int:
        """
        Counts total nodes in the subtree.
        """
        pass

    def count_leaf_nodes(self) -> int:
        """
        Counts leaf nodes in the subtree.
        """
        pass

    def is_balanced(self) -> bool:
        """
        Checks if the subtree is balanced (AVL property).
        """
        pass

    def lowest_common_ancestor(self, node1: int, node2: int) -> Optional[int]:
        """
        Finds LCA of two nodes in the subtree.
        """
        pass

    def serialize(self) -> list:
        """
        Converts the tree into a list or other serial format.
        """
        pass

    @staticmethod
    def deserialize(data: list) -> Optional["AVLNode"]:
        """
        Reconstructs an AVL tree from serialized data.
        """
        pass

from typing import Optional, Any

class RBNode:
    def __init__(self, number: int, color: str = "RED") -> None:
        """
        Initialize a Red-Black Tree node.
        Color is either "RED" or "BLACK".
        """
        self.number: int = number
        self.color: str = color
        self.left_pointer: Optional["RBNode"] = None
        self.right_pointer: Optional["RBNode"] = None
        self.parent: Optional["RBNode"] = None

    # ---------------- Utility Functions ----------------
    def is_red(self) -> bool:
        pass

    def is_black(self) -> bool:
        pass

    def get_sibling(self) -> Optional["RBNode"]:
        pass

    def get_uncle(self) -> Optional["RBNode"]:
        pass

    def get_grandparent(self) -> Optional["RBNode"]:
        pass

    # ---------------- Rotations ----------------
    def left_rotate(self) -> "RBNode":
        """
        Performs left rotation and returns new root of the subtree.
        """
        pass

    def right_rotate(self) -> "RBNode":
        """
        Performs right rotation and returns new root of the subtree.
        """
        pass

    # ---------------- RB Tree Operations ----------------
    def insert_node(self, number: int) -> "RBNode":
        """
        Inserts a node and fixes Red-Black properties.
        """
        pass

    def delete_node(self, number: int) -> Optional["RBNode"]:
        """
        Deletes a node and fixes Red-Black properties.
        """
        pass

    def search_node(self, number: int) -> Optional["RBNode"]:
        """
        Searches for a node with the given number.
        """
        pass

    # ---------------- Traversals ----------------
    def in_order_traversal(self) -> None:
        pass

    def pre_order_traversal(self) -> None:
        pass

    def post_order_traversal(self) -> None:
        pass

    def level_order_traversal(self) -> None:
        pass

    # ---------------- Extra Utilities ----------------
    def find_min(self) -> "RBNode":
        pass

    def find_max(self) -> "RBNode":
        pass

    def count_nodes(self) -> int:
        pass

    def count_leaf_nodes(self) -> int:
        pass

    def is_valid_rb_tree(self) -> bool:
        """
        Checks if subtree satisfies all Red-Black Tree properties.
        """
        pass

    def lowest_common_ancestor(self, node1: int, node2: int) -> Optional[int]:
        pass

    def serialize(self) -> list:
        pass

    @staticmethod
    def deserialize(data: list) -> Optional["RBNode"]:
        pass


from typing import List, Optional

class BTreeNode:
    def __init__(self, t: int, leaf: bool = True) -> None:
        """
        Initialize a B-Tree node.
        t: Minimum degree (defines the range for number of keys)
        leaf: True if node is a leaf
        """
        self.t: int = t
        self.leaf: bool = leaf
        self.keys: List[int] = []  # List of keys
        self.children: List[Optional["BTreeNode"]] = []  # List of child pointers

    # ---------------- Utility Functions ----------------
    def is_full(self) -> bool:
        """
        Checks if node has maximum keys.
        """
        pass

    def find_key_index(self, key: int) -> int:
        """
        Returns the index of the first key greater than or equal to key.
        """
        pass

    # ---------------- B-Tree Operations ----------------
    def insert_non_full(self, key: int) -> None:
        """
        Inserts a key into this node assuming it is non-full.
        """
        pass

    def split_child(self, i: int, y: "BTreeNode") -> None:
        """
        Splits the child y of this node at index i.
        """
        pass

    def insert(self, key: int) -> "BTreeNode":
        """
        Inserts a key into the B-Tree and returns the root.
        """
        pass

    def delete(self, key: int) -> Optional["BTreeNode"]:
        """
        Deletes a key from the subtree rooted with this node.
        """
        pass

    def search(self, key: int) -> Optional["BTreeNode"]:
        """
        Searches for a key in the subtree rooted with this node.
        """
        pass

    # ---------------- Traversals ----------------
    def traverse_in_order(self) -> None:
        pass

    def traverse_pre_order(self) -> None:
        pass

    def traverse_post_order(self) -> None:
        pass

    # ---------------- Extra Utilities ----------------
    def find_min(self) -> int:
        pass

    def find_max(self) -> int:
        pass

    def count_nodes(self) -> int:
        pass

    def count_leaf_nodes(self) -> int:
        pass

    def serialize(self) -> list:
        """
        Serialize the B-Tree to a list representation.
        """
        pass

    @staticmethod
    def deserialize(data: list, t: int) -> Optional["BTreeNode"]:
        """
        Deserialize list representation back to a B-Tree.
        """
        pass

from typing import List, Optional

class BPlusTreeNode:
    def __init__(self, t: int, leaf: bool = True) -> None:
        """
        Initialize a B+ Tree node.
        t: Minimum degree (defines the range for number of keys)
        leaf: True if node is a leaf
        """
        self.t: int = t
        self.leaf: bool = leaf
        self.keys: List[int] = []  # Only keys, values stored in leaf nodes
        self.children: List[Optional["BPlusTreeNode"]] = []  # Child pointers
        self.next: Optional["BPlusTreeNode"] = None  # Linked list pointer for leaf nodes

    # ---------------- Utility Functions ----------------
    def is_full(self) -> bool:
        """
        Checks if the node has maximum keys.
        """
        pass

    def find_key_index(self, key: int) -> int:
        """
        Returns the index of the first key greater than or equal to key.
        """
        pass

    # ---------------- B+ Tree Operations ----------------
    def insert_non_full(self, key: int, value: Optional[int] = None) -> None:
        """
        Inserts a key into a node assuming it is non-full.
        Value is stored in the leaf node.
        """
        pass

    def split_child(self, i: int, y: "BPlusTreeNode") -> None:
        """
        Splits the child y of this node at index i.
        """
        pass

    def insert(self, key: int, value: Optional[int] = None) -> "BPlusTreeNode":
        """
        Inserts a key-value pair into the B+ Tree and returns the root.
        """
        pass

    def delete(self, key: int) -> Optional["BPlusTreeNode"]:
        """
        Deletes a key from the subtree rooted with this node.
        """
        pass

    def search(self, key: int) -> Optional[int]:
        """
        Searches for a key in the B+ Tree and returns the value if found.
        """
        pass

    # ---------------- Traversals ----------------
    def traverse_in_order(self) -> None:
        """
        Traverses the leaf nodes using linked list.
        """
        pass

    def traverse_pre_order(self) -> None:
        """
        Traverses the tree top-down for structure inspection.
        """
        pass

    # ---------------- Extra Utilities ----------------
    def find_min(self) -> int:
        pass

    def find_max(self) -> int:
        pass

    def count_nodes(self) -> int:
        pass

    def count_leaf_nodes(self) -> int:
        pass

    def serialize(self) -> list:
        """
        Serialize the B+ Tree to a list representation.
        """
        pass

    @staticmethod
    def deserialize(data: list, t: int) -> Optional["BPlusTreeNode"]:
        """
        Deserialize list representation back to a B+ Tree.
        """
        pass

# Good. This idea is **the key that makes all AVL rotations trivial**. Once you see it, you stop memorizing LL/LR/RL/RR and just **rebuild the tree logically**.

# The rule is:

# > **Every AVL rotation only rearranges 3 nodes and 4 subtrees.**

# No matter how big the tree is.

# ---

# # The 3 Nodes

# When imbalance happens, only these nodes matter:

# ```
# A = first unbalanced node
# B = child of A in the heavy direction
# C = child of B in the direction where insertion happened
# ```

# So the structure always looks like one of these shapes.

# Example (LR case):

# ```
#         A
#        /
#       B
#        \
#         C
# ```

# But the **important thing isn't the nodes — it's the subtrees**.

# ---

# # The 4 Subtrees

# Every configuration can be expanded like this:

# ```
#         A
#        / \
#       B   T4
#      / \
#     T1  C
#        / \
#       T2 T3
# ```

# So the **entire tree around the imbalance** is actually:

# ```
# T1  B  T2  C  T3  A  T4
# ```

# That order is **sorted order** because this is a BST.

# So we know:

# ```
# T1 < B < T2 < C < T3 < A < T4
# ```

# That ordering **must never change**.

# ---

# # The Trick

# Instead of thinking about rotations, think:

# > **What node should be the new root of these three nodes while preserving sorted order?**

# Look at the middle value.

# ```
# B < C < A
# ```

# So **C must become the root**.

# That immediately gives the final structure:

# ```
#         C
#        / \
#       B   A
# ```

# Now we just place the subtrees.

# ---

# # Reattach Subtrees Using the Sorted Rule

# We still must respect:

# ```
# T1 < B < T2 < C < T3 < A < T4
# ```

# So:

# ```
# B.left  = T1
# B.right = T2

# A.left  = T3
# A.right = T4
# ```

# Final tree:

# ```
#         C
#        / \
#       B   A
#      / \ / \
#     T1 T2 T3 T4
# ```

# Done.

# No memorization needed.

# ---

# # Why this works for *every* rotation

# Because all AVL cases reduce to the same **3-node sorted set**.

# ### LL case

# ```
# C < B < A
# ```

# Middle = **B**

# So B becomes root.

# ---

# ### RR case

# ```
# A < B < C
# ```

# Middle = **B**

# So B becomes root.

# ---

# ### LR case

# ```
# B < C < A
# ```

# Middle = **C**

# So C becomes root.

# ---

# ### RL case

# ```
# A < C < B
# ```

# Middle = **C**

# So C becomes root.

# ---

# # This is how experienced engineers think

# Not:

# ```
# LL → right rotate
# LR → left then right
# ```

# Instead:

# 1. Identify **A, B, C**
# 2. Sort them
# 3. Promote the **middle node**
# 4. Reattach **T1 T2 T3 T4**

# That's it.

# ---

# # Why this matters beyond AVL

# This mental model is also used in:

# * **Red-Black Trees**
# * **Treaps**
# * **Splay Trees**
# * **B-Trees (generalized version)**

# So what you just learned is actually a **general balancing principle**, not just AVL.

# ---

# If you want, I can also show you something interesting:

# **Why AVL trees mathematically guarantee height ≤ 1.44 log₂(n)**

# This proof is surprisingly elegant and explains **why AVL trees are so fast**.

