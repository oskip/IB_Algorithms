# Please Note:
#
# Note: It is intended for some problems to be ambiguous. You should gather all requirements up front before implementing one.
#
# Please think of all the corner cases and clarifications yourself.
#
# Validate if a given string is numeric.
#
# Examples:
#
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem
#
# Clarify the question using "See Expected Output"
#
# Is 1u ( which may be a representation for unsigned integers valid?
# For this problem, no.
# Is 0.1e10 valid?
# Yes
# -01.1e-10?
# Yes
# Hexadecimal numbers like 0xFF?
# Not for the purpose of this problem
# 3. (. not followed by a digit)?
# No
# Can exponent have decimal numbers? 3e0.1?
# Not for this problem.
# Is 1f ( floating point number with f as prefix ) valid?
# Not for this problem.
# How about 1000LL or 1000L ( C++ representation for long and long long numbers )?
# Not for this problem.
# How about integers preceded by 00 or 0? like 008?
# Yes for this problem


class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        if len(A) < 1: return False
        # One dot and not last
        if A.count(".") > 1 or A[len(A)-1] == "." or A[len(A)-1] == "e": return False
        # Only digits, dot or 'e' from second char
        for c in A[1:]:
            if ord('0') <= ord(c) <= ord('9') or c in [".", "-", "+", "e"]:
                continue
            else: return False
        # One plus or minus or number at start
        if A[0] not in ["+", "-", "."] and not (ord('0') <= ord(A[0]) <= ord('9')):
            return False
        if ("+" in A or "-" in A) and len(A) < 2: return False
        if "e" in A:
            for c in A[A.index("e")+1:]:
                if not (ord('0') <= ord(c) <= ord('9')) and c != "-": return False
        if ".e" in A: return False
        return True


print Solution().isNumber("1.e1")