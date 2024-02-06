### Combination ###

# version1
def combination(n, r):
    ans = []

    def recur(start, tmp_ans):
        if len(tmp_ans) == r:
            ans.append(tmp_ans[:])
            return
        for i in range(start, n+1):
            tmp_ans.append(i)
            recur(i+1, tmp_ans)
            tmp_ans.pop()
        
    recur(1, [])
    return ans

# Examples
print(combination(4, 2))
print(len(combination(7, 3)), combination(7, 3)) 
