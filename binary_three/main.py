class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data

    def __str__(self) -> str:
        # TODO: Print the left and right values
        return str(self.data)


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

    def getHeight(self, root: Node):
        # Write your code here
        print("Height")
        print(root)
        pass

    # https://stackoverflow.com/questions/2597637/finding-height-in-binary-search-tree


def main() -> None:
    print('Start program')
    T = int(input())
    print('Number to insert: ', T)
    myTree = Solution()
    root = None
    for i in range(T):
        data = int(input())
        root = myTree.insert(root, data)
    height = myTree.getHeight(root)
    print(height)


if __name__ == "__main__":
    main()
