"""
Context:
A Node object has an integer data field,data , and a Node instance pointer, next, 
pointing to another node (i.e.: the next node in a list).

Constraints:
The data elements of the linked list argument will always be in non-decreasing order.

Output Format:
Your removeDuplicates function should return the head of the updated linked list. 
The locked stub code in your editor will print the returned list to stdout.

Ref: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem?isFullScreen=true
"""


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        # The first iteration
        if head == None:
            head = p
        # The next Node: The second one
        elif head.next == None:
            head.next = p
        else:
            # The head being
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head: Node):
        start = head
        while start:
            print(start.data, end=' ')
            start = start.next

    # NOTE: Just copy the removeDuplicates content
    def removeDuplicates(self, head: Node) -> Node:
        """Takes a pointer to the head node of a linked list as a parameter. 
        Complete removeDuplicates so that it deletes any duplicate nodes from 
        the list and returns the head of the updated list"""
        if head is None:
            return None

        # The last value to check out if should be removed

        start = head
        lastValue = start.data
        # TODO: Draw and understan the problem
        # Iterates over the node
        while (start.next != None):
            # This node always is not None
            nextNode = start.next
            if lastValue == nextNode.data:
                start.next = None
            start = nextNode.next
        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
