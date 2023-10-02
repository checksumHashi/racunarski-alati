class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(self, head):
    s = set()
    curr = head        
    while curr:
        if curr in s:
            return True
        else:
            s.add(curr)
        curr = curr.next
    
    return False

p = ListNode(1)
q = ListNode(2)
r = ListNode(3)
t = ListNode(7)
o = ListNode(3)
p.next = q
q.next = r
r.next = t
t.next = o
o.next = None
print(hasCycle(head = p))
