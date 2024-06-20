class Node:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None
        

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

# temp = Node("INSERT")

#For example, i want to insert it at index 1 (Between b and c)
# cur = b
# cur.next = temp
# temp.next = c

# cur = head

# while(cur):
#     arr.append(cur.val)
#     cur = cur.next

# def iterate(cur):
#     if cur == None:
#         return
    
#     print(cur.val)
#     iterate(cur.next)
# iterate(head)

