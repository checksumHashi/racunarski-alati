class listnode:
    def __init__(self, val):
        self.val = val
        self.next = None

p = listnode(1)
q = listnode(2)
r = listnode(3)
t = listnode(7)
o = listnode(3)
p.next = q
q.next = r
r.next = t
t.next = o
o.next = None

def check():
    curr = p
    s = set()
    while curr:
        if curr in set():
            return True
        else:
            set.add(curr)
        curr = curr.next

print(check())