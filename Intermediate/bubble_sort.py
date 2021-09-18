import time
import random


def bubble_sort(nums):
    time_start = time.time()
    print("Bubble Sort")
    #print(nums, "\n")
    for i in range(len(nums)-1):
        #    print("Iteration ", i+1)
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    #        print(nums)
    time_end = time.time()
    time_delta = time_end - time_start
    return (time_delta)


def optimized_bubble_sort(nums):
    time_start = time.time()
    print("Optimized Bubble Sort")
    is_swapped = True
    nums_of_iterations = 0
    while(is_swapped):
        is_swapped = False
    #    print("Iteration ", nums_of_iterations+1)
        for j in range(len(nums)-1-nums_of_iterations):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                is_swapped = True
    #        print(nums)
        nums_of_iterations += 1
    time_end = time.time()
    time_delta = time_end - time_start
    return (time_delta)


nums = [8, 5, 3, 1, 4, 7, 6]

for i in range(10000):
    nums.append(random.randrange(0, 100000))
nums2 = nums.copy()
print(bubble_sort(nums))
print(optimized_bubble_sort(nums2))
