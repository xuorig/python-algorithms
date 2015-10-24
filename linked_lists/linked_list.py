class Node(object):
    def __init__(self, item, next):
        self.item = item
        self.next = next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def empty(self):
        return self.head == None

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def find(self, x):
        current = self.head
        while current:
            if current.item == x:
                return current
            current = current.next
        return None

    def findNth(self, index):
        current = self.head
        i = 0
        while current:
          if i == index:
              return current
          current = current.next
          i += 1
        return None

    def pop(self):
        if self.empty():
            return None
        poped = self.head.item
        self.head = self.head.next
        return poped

    def findNthToLast(self, n):
        if n <= 0:
            return None

        p1 = self.head
        p2 = self.head

        for i in range(k - 1):
            if p2 == None:
                return None
            p2 = p2.next

        if p2 == None:
            return None

        while p2.next:
            p1 = p1.next
            p2 = p2.next

        return p1

    # Remove duplicates using a map for constant time lookup
    # Takes space though
    def removeDuplicates(self):
        count = {}
        current = self.head
        prev = None
        while current:
            if count.get(current.item):
                prev.next = current.next
            else:
                count[current.item] = True
                prev = current
            current = current.next

    # Remove the duplicates using no extra space
    # Using a runner pointer
    def removeDuplicates2(self):
        if self.empty():
            return
        runner = self.head
        current = self.head
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def append(self, item):
        # TODO
    def insertNth(self, item, n):
        # TODO
    def sortedInsert(self, item):
        # TODO
    def reverse(self):
        # TODO
    def recursiveReverse(self):
        # TODO
    def deleteMiddle(self):
        # TODO
    def findLoopBegin(self):
        # TODO
    def isPalindrome(self):
        # TODO
