### Combination ###

# version1
def combination(nums, r):
    if isinstance(nums, int):
        nums = [x for x in range(1, nums+1)]
    elif not isinstance(nums, (list, tuple)):
        raise "Inappropriate data structure! Only integer, iterable object(list, tuple but not string here)"

    ans = []

    def recur(start, tmp_ans):
        if len(tmp_ans) == r:
            ans.append(tmp_ans[:])
            return
        for i in range(start, len(nums)):
            tmp_ans.append(nums[i])
            recur(i+1, tmp_ans)
            tmp_ans.pop()
        
    recur(0, [])
    return ans

# Examples
print(combination(4, 2))
print(len(combination(7, 3)), combination(7, 3)) 
print(combination([3, 5, 18, 9], 2))

print(combination(1, 1))
print(combination(2, 3))

