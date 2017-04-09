class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if ipv4(IP):
            return 'IPv4'
        if ipv6(IP):
            return 'IPv6'
        return 'Neither'

def ipv4(ip):
    if '.' not in ip:
        return False
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not (1 <= len(part) <= 3):
            return False
        if not all(c.isdigit() for c in part):
            return False
        if part[0] == '0' and part != '0':
            return False
        if not (0 <= int(part) <= 255):
            return False
    return True

def ipv6(ip):
    if ':' not in ip:
        return False
    parts = ip.split(':')
    if len(parts) != 8:
        return False
    for part in parts:
        if not (1 <= len(part) <= 4):
            return False
        if not all(c.lower() in '0123456789abcdef' for c in part):
            return False
    return True
