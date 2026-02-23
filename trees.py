# 50, 30, 70, 60, 80, 65
from typing import Optional, Any
class Node:
    def __init__(self, number: int) -> None:
        self.number = number
        self.leftPointer: Node | None = None
        self.rightPointer: Node | None = None

    # BST operations
    def insertNode(self, number):

        if number > self.number:
            if self.rightPointer is None:
                self.rightPointer = Node(number=number)
            else:
                self.rightPointer.insertNode(number=number)
        elif number < self.number:
            if self.leftPointer is None:
                self.leftPointer = Node(number=number)
            else:
                self.leftPointer.insertNode(number=number)

    def searchNode(self, number) -> Any:
        pass

    def deleteNode(self, number):
        pass

    # BST Traversals
    def preOrderTraversal(self):
        pass

    def inOrderTraversal(self):
        pass

    def postOrderTraversal(self):
        pass

    def levelOrderTraversal(self):
        pass

    # Utilities
    def getHeight(self) -> Any:
        pass

    def countNodes(self) -> Any:
        pass

    def countLeafNodes(self) -> Any:
        pass

    def findMin(self) -> Any:
        pass

    def findMax(self) -> Any:
        pass

    def lowestCommonAncestor(self, node1, node2):
        pass

    def isBalanced(self) -> Any:
        pass

    def diameter(self) -> Any:
        pass

    def pathSum(self, target: int) -> Any:
        pass

    def serialize(self) -> Any:
        pass

    def deserialize(self, data: Any):
        pass


rootNode = Node(10)
rootNode.insertNode(12)

