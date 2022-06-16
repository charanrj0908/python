def sort(nums):
    for i in range(len(nums)-1):
        min = i
        for j in range(i+1,len(nums)):
            if nums[j] < nums[min]:
                min = j


        temp = nums[i]
        nums[i]=nums[min]
        nums[min] = temp

nums = [7,4,10,8,3,1]
sort(nums)
print(nums)