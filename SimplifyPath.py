# Given an absolute path for a file (Unix-style), simplify it.
#
# Examples:
#
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# Note that absolute path always begin with '/' ( root directory )
# Path will not have whitespace characters.


class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        A = A+"/"
        curPath = ""
        pathStack = []
        for a in A:
            if a == "/":
                if curPath == ".." and len(pathStack) > 0: pathStack.pop()
                elif curPath not in [".","",".."]: pathStack.append(curPath)
                curPath = ""
            else: curPath += a
        if len(curPath) > 0 and curPath not in [".","",".."]: pathStack.append(curPath)
        res = "/"+"/".join(pathStack)
        return res


print Solution().simplifyPath("/./.././ykt/xhp/nka/eyo/blr/emm/xxm/fuv/bjg/./qbd/./../pir/dhu/./../../wrm/grm/ach/jsy/dic/ggz/smq/mhl/./../yte/hou/ucd/vnn/fpf/cnb/ouf/hqq/upz/akr/./pzo/../llb/./tud/olc/zns/fiv/./eeu/fex/rhi/pnm/../../kke/./eng/bow/uvz/jmz/hwb/./././ids/dwj/aqu/erf/./koz/..")
