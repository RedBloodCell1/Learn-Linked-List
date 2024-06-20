from linkedList import Node

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e

head = a

def insertToArray(head):
    arr = []
    insertToArray2(head, arr)
    return arr

def insertToArray2(cur, arr):
    if cur == None: return
    arr.append(cur.val)
    return insertToArray2(cur.next, arr)

print(insertToArray(head))