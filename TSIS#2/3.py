nums = [1,2,3,1,1,3]
cnt = i = j = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] == nums[j] and i < j:
            cnt += 1
print(cnt)