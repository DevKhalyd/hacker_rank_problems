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
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
        p = Node(data)
        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while(start.next != None):
                start = start.next
            start.next = p
        return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    # NOTE: Just copy the removeDuplicates content
    def removeDuplicates(self, head: Node) -> Node:
        """Takes a pointer to the head node of a linked list as a parameter. 
        Complete removeDuplicates so that it deletes any duplicate nodes from 
        the list and returns the head of the updated list"""
        if head is None:
            return None

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
head = mylist.removeDuplicates(head)
mylist.display(head)
