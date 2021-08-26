
class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

    def __str__(self) -> str:
        data = self.data
        right = self.right
        left = self.left
        return str(left) + str(data) + str(right)

    def printDef(self) -> None:
        definition = self.__str__()
        print(definition)


class Solution:
    def insert(self, root: Node, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    # https://stackoverflow.com/a/2597754/10942018
    # Basically here I learned the concept of the binary three search
    # Check other section in this repo to see my own solutions for this one
    def getHeight(self, root: Node) -> int:
        if root is None:
            return -1
        lefth = self.getHeight(root.left)
        righth = self.getHeight(root.right)
        if lefth > righth:
            return lefth + 1
        else:
            return righth + 1

def main() -> None:
    T = int(input())
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    # TODO: Uncomment this
    height = myTree.getHeight(root)
    print(height)

if __name__ == "__main__":
    main()
