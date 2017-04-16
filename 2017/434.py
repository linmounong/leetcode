class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        state = 0
        for c in s:
            sp = c == ' '
            if state == 0:
                if sp:
                    state = 1
                else:
                    state = 2
                    ret += 1
            elif state == 1:
                if not sp:
                    state = 2
                    ret += 1
            else:
                if sp:
                    state = 1
        return ret
