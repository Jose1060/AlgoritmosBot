class Node:
    def __init__(self):          #   # Constructor
        self.data = None
        self.next = None
    def setData(self, data):      # Method for setting the data
        self.data = data
    def getData(self):            # Method for getting the data
        return self.data
    def setNext(self, next):        # Method for setting the pointer
        self.next = next
    def getNext(self):                # Method for getting the pointer
        return self.next
    def hasNext(self):                # return true if the node point to another node
        return self.next != None

class LinkedList :
    def __init__(self):   # Constructor
        self.head = None
        self.length = 0

    def print( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
        print("NULL")
    # Insert an item at the begin
    def insertAtBegin(self,data):

        newNode = Node()
        newNode.setData(data)

        if self.length == 0:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

        self.length += 1

    def insertAtEnd(self,data):

        newNode = Node()
        newNode.setData(data)

        current = self.head

        while current.getNext() != None:
            current = current.getNext()

        current.setNext(newNode)
        self.length += 1

    # Method for inserting a new node at any position in a Linked List
    def insertAtPos(self,pos,data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insertAtBegin(data)
            else:
                if pos == self.length:
                    self.insertAtEnd(data)
                else:
                    newNode = Node()
                    newNode.setData(data)
                    count = 0
                    current = self.head
                    while count< pos-1:
                        count+= 1
                        current = current.getNext()

                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self.length += 1
    def clear( self) :
        self.head = None

    def print( self):
        count = 0
        current = self.head
        while not current.getNext() == None:
            count+= 1
            print (current.data)
            current = current.getNext()
            


"""


ejemplo = LinkedList()
ejemplo.insertAtBegin(10)
ejemplo.insertAtBegin(20)
ejemplo.insertAtBegin(30)
ejemplo.insertAtBegin(40)
#ejemplo.print()

t = LinkedList()
t.insertAtBegin(50)
t.insertAtBegin(51)
t.insertAtBegin(52)
t.insertAtBegin(53)
t.insertAtBegin(54)
#t.print()

ejemplo.print()
print(ejemplo.length)
print(ejemplo.head.data)


"""
"""
x = LinkedList()
a = [10, 20, 30, 40, 41, 42, 43, 44, 45,  50, 51, 52 , 53, 54]
for i in range(len(a)):
  x.insertAtPos(i, a[i])
x.print()
"""

print("-----------------------------")
"""
#a.LinkedList.clear()
#LinkedList.clear(x)
#LinkedList.clear(t)
#x.print()
#t.print()
#ejemplo.print()
"""