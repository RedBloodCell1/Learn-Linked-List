from linkedList import Node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

head = a

arr = []

def insertToArray(head):
    cur = head
    while(cur):
        arr.append(cur.val)
        cur = cur.next

insertToArray(head)
print(arr)
