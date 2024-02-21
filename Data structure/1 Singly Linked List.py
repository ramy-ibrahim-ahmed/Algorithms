class LinkedNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        curr = LinkedNode(val)
        curr.next = self.head.next
        self.head.next = curr
        if not curr.next:
            self.tail = curr

    def insertTail(self, val: int) -> None:
        self.tail.next = LinkedNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            dumb = curr.next
            curr.next = curr.next.next
            del dumb
            return True
        return False

    def getValues(self) -> list[int]:
        curr = self.head.next
        l = []
        while curr:
            l.append(curr.val)
            curr = curr.next
        return l


"""
Input: 
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]
"""
l = LinkedList()
l.insertHead(1)  # [0, 1, 2]
l.insertTail(2)
l.insertHead(0)
l.remove(1)
print(l.getValues())

"""
Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]
"""
l.insertHead(1)
l.insertHead(2)
print(l.get(5))