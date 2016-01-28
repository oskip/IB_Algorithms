import itertools

class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        return self.getIp([], "", 4, A)

    def getIp(self, list, prev, rem, num):
        num = str(num)
        if rem == 0: list.append(prev[:-1])
        if rem <= len(num) <= rem * 3:
            rem -= 1
            if rem <= len(num) - 1 <= rem * 3:
                self.getIp(list, prev+num[0] + ".", rem, num[1:])
            if rem <= len(num) - 2 <= rem * 3 and num[0] != "0":
                self.getIp(list, prev+num[0] + num[1] + ".", rem, num[2:])
            if rem <= len(num) - 3 <= rem * 3 and int(num[0] + num[1] + num[2]) <= 255 and num[0] != "0":
                self.getIp(list, prev+num[0] + num[1] + num[2] + ".", rem, num[3:])
        else: return
        return list

print Solution().restoreIpAddresses("1411123")