# Problem 1
# Given a list of integers, return True if the sequence of numbers 1, 2, 3  appears in the list somewhere.
# For example:
# arrayCheck([1, 1, 2, 3, 1]) → True arrayCheck([1, 1, 2, 4, 1]) → False arrayCheck([1, 1, 2, 1, 2, 3]) → True



# def arrayCheck(num_list):
#     items = set(num_list)
#     result = set([1, 2, 3]).issubset(items)

#     if result:
#         print("True")
#     else:
#         print("False")


# arrayCheck([1, 1, 2, 3, 1])
# arrayCheck([1, 1, 2, 4, 1])
# arrayCheck([1, 1, 2, 1, 2, 3])


def arrayCheck(num_list):
    result = set([1, 2, 3]).issubset(num_list)
    if result:
        print("True")
    else:
        print("False")

arrayCheck([1, 1, 2, 3, 1])
arrayCheck([1, 1, 2, 4, 1])
arrayCheck([1, 1, 2, 1, 2, 3])


# def array123(nums):
#   # Note: iterate with length-2, so can use i+1 and i+2 in the loop
#   for i in range(len(nums)-2):
#     if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
#       return True
#   return False







    



