#task1
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
            return self.head is None

    def append(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp


    def index(self, item):
        curr = self.head

        while curr is not None:
            if curr.value == item:
                return True
            curr = curr.next

        return False

    def pop(self, item):
        curr = self.head
        previous = None

        while True:
            if curr.value == item:
                break
            previous, current = curr, curr.next

        if previous is None:
            self.head = curr.next
        else:
            previous.next = curr.next


class Queue:

    def __init__(self):
        self.head = self.rear = None

    def is_empty(self):
        return self.head == None


    def queue(self, item):
        temp = Node(item)

        if self.rear == None:
            self.head = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp


    def remove_queue(self):

        if self.is_empty():
            return
        temp = self.head
        self.head = temp.next

        if (self.head == None):
            self.rear = None
