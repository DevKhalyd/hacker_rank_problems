import sys


class Solution:

    stack = []
    queue = []

    def pushCharacter(self, char: str) -> None:
        """Push a character onto a stack defined"""
        self.stack.append(char)

    def enqueueCharacter(self, char: str) -> None:
        """Enqueue a character in the queue variable"""
        #self.queue.insert(0, char)
        self.queue.append(char)

    def popCharacter(self) -> str:
        """Pops and returns the character at the top of the stack instance variable"""
        s = self.stack
        return s.pop()

    def dequeueCharacter(self) -> str:
        """Dequeue and returns the first character in the queue instance variable"""
        q = self.queue
        firstValue = q[0]
        if len(q) > 0:
            del q[0]
        return firstValue


# TODO Read the docs again
# https://code.visualstudio.com/docs/editor/debugging#_logpoints
# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

print("After of fill the new data the loop")
print(obj.stack)
print(obj.queue)


isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
# Return the halt of l
iterates = range(l // 2)


print("Iterating the loop")

for i in iterates:
    # To debug in VS code use this sintax
    popCharacter = obj.popCharacter()
    print("Stack")
    print(obj.stack)
    dequeueCharacter = obj.dequeueCharacter()
    print("Queue")
    print(obj.queue)
    if popCharacter != dequeueCharacter:
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")
