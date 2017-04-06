import string

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        state = 0
        for c in word:
            state = next_state(state, c)
            if state == -1:
                return False
        return True

def next_state(state, c):
    cap = c in string.ascii_uppercase
    if state == 0:
        return 2 if cap else 1
    if state == 1:
        return -1 if cap else 1
    if state == 2:
        return 4 if cap else 3
    if state == 3:
        return -1 if cap else 3
    if state == 4:
        return 4 if cap else -1
