class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

cur = a

while(cur):
    print(cur.val)
    cur = cur.next

