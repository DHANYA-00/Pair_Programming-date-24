def GenerateParenthesis(n):
    sol = []

    def backtrack(res,left,right):
        if len(res) == n*2:
            sol.append(res[:])
            return

            
        if left < n:
            backtrack(res+"(",left+1,right)
        if right < left:
            backtrack(res+")",left,right+1)
    backtrack("",0,0)
    return sol

n = int(input())
print(GenerateParenthesis(n))
