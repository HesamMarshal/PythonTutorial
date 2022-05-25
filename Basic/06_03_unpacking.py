##########################################
# This code is created by Hesam Marshal  #
# Website : Chaptera.ir                  #
# instagram: @HesamMarshal               #
# List unpacking                         #
##########################################

nums = [1, 2, 3]
# print(nums)
# first = nums[0]
# second = nums[1]
# third = nums[2]
# print(first)

# first, second, third = nums
# print(first)

# first, second = nums

first, second, _ = nums
# print(first)

nums = [1, 2, 3, 4, 5, 6, 7]
print(nums)
first, second, *others = nums
first, second, *others, last = nums

print(first)
print(second)
print(others)
print(last)
