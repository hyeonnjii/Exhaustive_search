### Permutation ###

def permutation(nums, r):
    if isinstance(nums, int):
        nums = [x for x in range(1, nums+1)]
    elif not isinstance(nums, (list, tuple)):
        raise "Invalid Data Struture Argument! Try interger, list or tuple:)"


    ans = []


    def recur(tmp_ans):
        if len(tmp_ans) == r:
            ans.append(tmp_ans[:])
            return

        for i in range(0, len(nums)):
            if nums[i] not in tmp_ans:
                tmp_ans.append(nums[i])
                recur(tmp_ans)
                tmp_ans.pop()
    recur([])
    return ans

# Examples
print(permutation(5, 2))
print(permutation([1, 3, 5, 9], 3))
print(permutation(1, 1))
print(permutation(3, 4))
