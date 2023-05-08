'''

    Design Pattern 5: Behavioral Patterns - Iterator.

'''

class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

# Define an iterator that can be applied in for loop.
class LinkedList:

    def __init__(self, head):
        self.head = head
        self.cur = None

    # Define iterator
    def __iter__(self):
        self.cur = self.head
        return self    

    # Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    myList = LinkedList(head)

    for n in myList:
        print(n)