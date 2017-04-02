class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        state = {}
        for i in range(1, N + 1):
            state[i] = set(j for j in range(1, N + 1) if valid(i, j))
        return foo(state)

def foo(state):
    if not state:
        return 1
    i = min(state, key=lambda i: len(state[i]))
    place = state[i]
    del state[i]
    ret = 0
    for j in place:
        ss = []
        for _, s in state.iteritems():
            if j in s:
                s.remove(j)
                ss.append(s)
        ret += foo(state)
        for s in ss:
            s.add(j)
    state[i] = place
    return ret
        
def valid(i, j):
    return i % j == 0 or j % i == 0
