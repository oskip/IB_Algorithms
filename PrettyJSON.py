# Pretty print a json object using proper indentation.
#
# Every inner brace should increase one indentation to the following lines.
# Every close brace should decrease one indentation to the same line and the following lines.
# The indents can be increased with an additional '\t'
# Example 1:
#
# Input : {A:"B",C:{D:"E",F:{G:"H",I:"J"}}}
# Output :
# {
#     A:"B",
#     C:
#     {
#         D:"E",
#         F:
#         {
#             G:"H",
#             I:"J"
#         }
#     }
# }
# Example 2:
#
# Input : ["foo", {"bar":["baz",null,1.0,2]}]
# Output :
# [
#     "foo",
#     {
#         "bar":
#         [
#             "baz",
#             null,
#             1.0,
#             2
#         ]
#     }
# ]
# [] and {} are only acceptable braces in this case.
#
# Assume for this problem that space characters can be done away with.
#
# Your solution should return a list of strings, where each entry corresponds to a single line. The strings should not have “\n” character in them.


class Solution:
    # @param A : string
    # @return a list of strings
    def prettyJSON(self, A):
        lines = []
        line = ""
        i = 0
        indentLevel = 0
        while i < len(A):
            if A[i] == "[" or A[i] == "{":
                if len(line) > indentLevel: lines.append(line)
                lines.append(self.indent(A[i], indentLevel))
                indentLevel += 1
                line = self.indent("", indentLevel)
            elif A[i] == "]" or A[i] == "}":
                if len(line) > indentLevel: lines.append(line)
                indentLevel -= 1
                line = self.indent(A[i], indentLevel)
            elif A[i] == ",":
                lines.append(line+",")
                line = self.indent("", indentLevel)
            elif A[i] != " ":
                if len(line) > 0 and (line[-1] == "}" or line[-1] == "]"):
                    lines.append(line)
                    line = self.indent("", indentLevel)
                line += A[i]
            i += 1
        if line > indentLevel: lines.append(line)
        return lines

    def indent(self, line, level):
        for i in range(0,level):
            line = "\t" + line
        return line


print Solution().prettyJSON("{\"attributes\":[{\"nm\":\"ACCOUNT\",\"lv\":[{\"v\":{\"Id\":null,\"State\":null},\"vt\":\"java.util.Map\",\"cn\":1}],\"vt\":\"java.util.Map\",\"status\":\"SUCCESS\",\"lmd\":13585},{\"nm\":\"PROFILE\",\"lv\":[{\"v\":{\"Party\":null,\"Ads\":null},\"vt\":\"java.util.Map\",\"cn\":2}],\"vt\":\"java.util.Map\",\"status\":\"SUCCESS\",\"lmd\":41962}]}")
