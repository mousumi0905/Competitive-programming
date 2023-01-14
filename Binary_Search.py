#Given an array of integers nums which is sorted in
#  ascending order, and an integer target, 
# write a function to search target in nums. If target exists,
#  then return its index. Otherwise, return -1.
def search(nums, target):
        start=0
        end=len(nums)-1
        mid=int((start+end)/2)
        while not(nums[mid]==target) and start<=end:
           if target < nums[mid]:
               end = mid - 1
           else:
               start = mid + 1 
           mid = int((start+end)/2)
        if target==nums[mid]:
            return mid
        else:
            return -1
search([-1,0,3,5,9,12],  9)