class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        i = 0
        result = []
        while i < len(A):
            line = A[i]
            i += 1
            leftChars = B-len(line)
            while i < len(A) and leftChars >= len(A[i])+1:
                leftChars -= len(A[i])+1
                line = line + " " + A[i]
                i += 1
            spaces = B - len(line)
            lineWords = line.split(" ")
            j = 0
            if i < len(A) and len(lineWords) > 1:
                while spaces > 0:
                    lineWords[j] = lineWords[j] + " "
                    spaces -= 1
                    j = (j+1)%(len(lineWords)-1)
            else:
                while spaces > 0:
                    lineWords[-1] += " "
                    spaces -= 1
            result.append(" ".join(lineWords))
        return result


print Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)