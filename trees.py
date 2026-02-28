# 50, 30, 70, 60, 80, 65
from typing import Optional, Any
from collections import deque
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
        print(f"--{self.number}--")
        if self.leftPointer is not None:
            self.leftPointer.preOrderTraversal()
        if self.rightPointer is not None:
            self.rightPointer.preOrderTraversal()

    def inOrderTraversal(self):
        if self.leftPointer is not None:
            self.leftPointer.inOrderTraversal()
        print(f"--{self.number}--")
        if self.rightPointer is not None:
            self.rightPointer.inOrderTraversal()  

    def postOrderTraversal(self):
        if self.leftPointer is not None:
            self.leftPointer.postOrderTraversal()
        if self.rightPointer is not None:
            self.rightPointer.postOrderTraversal()  
        print(f"--{self.number}--")

    # Since this is BFS, it is done by queue
    def levelOrderTraversal(self):
        queue = deque()
        queue.append(self)
        while queue:
            popped = queue.popleft()
            print(popped.number)
            if popped.leftPointer is not None:
                queue.append(popped.leftPointer)
            if popped.rightPointer is not None:
                queue.append(popped.rightPointer)

    # Utilities
    arr: list[dict[str, int]] = []
    def getHeight(self) -> Any:
        if self.leftPointer is None and self.rightPointer is None:
            return { "node": self.number, "height": 0 }
        if self.leftPointer is not None:
            returned =  self.leftPointer.getHeight()
            return { "node": self.number, "height": None }
        if self.rightPointer is not None:
            returned =  self.rightPointer.getHeight()
            return { "node": self.number, "height": None }

    def countNodes(self) -> Any:
        pass

    def countLeafNodes(self) -> Any:
        pass

    def findMin(self) -> Any:
        # newSelf = self
        # while True:     
        #     if newSelf.leftPointer is not None:
        #         newSelf = newSelf.leftPointer
        #         continue
        #     if newSelf.leftPointer is None:
        #         print("the smallest is ", newSelf.number)
        #         return newSelf.number
        #     break
        if self.leftPointer is not None:
            return self.leftPointer.findMin()
        return self.number

    def findMax(self) -> Any:
        if self.rightPointer is not None:
            return self.rightPointer.findMax()
        return self.number
        

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
rootNode.insertNode(5)
rootNode.insertNode(3)
rootNode.insertNode(7)
rootNode.insertNode(15)
rootNode.insertNode(13)
rootNode.insertNode(17)
print(rootNode.getHeight())

