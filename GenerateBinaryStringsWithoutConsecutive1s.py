class Solution:
    def generateBinaryStrings(self, n):
        result = []

        def backtrack(curr):
            if len(curr) == n:
                result.append(curr)
                return
            
            backtrack(curr + "0")
            
            if not curr or curr[-1] != "1":
                backtrack(curr + "1")

        backtrack("")
        return result
