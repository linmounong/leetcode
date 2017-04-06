class Solution(object):

    def findMaximizedCapital(self, k, W, Profits, Capital):
        """
        :type k: int
        :type W: int
        :type Profits: List[int]
        :type Capital: List[int]
        :rtype: int
        """
        data = zip(Profits, Capital)
        data.sort(key=lambda o: o[1])
        h = MaxHeap()
        cap = W
        def update():
            while data and data[0][1] <= cap:
                h.add(data[0][0])
                data.pop(0)
            return h.size() > 0
        while k > 0 and update():
            cap += h.pop()
            k -= 1
        return cap
            
        
class MaxHeap(object):
    
    def __init__(self):
        self._l = []
        
    def add(self, o):
        l = self._l
        l.append(o)
        i = len(l) - 1
        while i > 0:
            j = (i - 1) // 2
            if l[j] > l[i]:
                break
            l[i], l[j] = l[j], l[i]
            i = j
    
    def pop(self):
        l = self._l
        if not l:
            return None
        ret = l[0]
        l[0] = l[-1]
        del l[-1]
        n = len(l)
        i = 0
        while True:
            j1 = 2 * i + 1
            j2 = j1 + 1
            if j1 >= n:
                break
            if j2 >= n:
                j = j1
            else:
                j = j1 if l[j1] > l[j2] else j2
            if l[i] > l[j]:
                break
            l[i], l[j] = l[j], l[i]
            i = j
        return ret
        
    def size(self):
        return len(self._l)
