def sort(nums):
    for i in range(len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp


nums=[8,3,1,6,7,2]
sort(nums)
print(nums)