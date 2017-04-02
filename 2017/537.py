class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r_a, i_a = parse(a)
        r_b, i_b = parse(b)
        r = r_a * r_b - i_a * i_b
        i = r_a * i_b + r_b * i_a
        return '{}+{}i'.format(r, i)

def parse(s):
    idx = s.find('+')
    return int(s[:idx]), int(s[idx + 1: -1])
