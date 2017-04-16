class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    r1 = list(it(l1))
    r1.reverse()
    n1 = len(r1)
    r2 = list(it(l2))
    r2.reverse()
    n2 = len(r2)

    i = forward = 0
    ret = []
    maxi = max(n1, n2)
    while i < maxi:
      v1 = r1[i].val if i < n1 else 0
      v2 = r2[i].val if i < n2 else 0
      ret.append(v1 + v2 + forward)
      if ret[-1] >= 10:
        ret[-1] -= 10
        forward = 1
      else:
        forward = 0
      i += 1
    if forward:
      ret.append(1)
    return toll(reversed(ret))

def it(ll):
  while ll:
    yield ll
    ll = ll.next

def toll(l):
  head = ListNode(None)
  i = head
  for o in l:
    i.next = ListNode(o)
    i = i.next
  return head.next
