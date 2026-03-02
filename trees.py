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
