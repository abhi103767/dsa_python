nums = [5]
import math;

# binary search apply on sorted array;




def search(nums,target):
    left = 0;
    right = len(nums) -1; 
    ans = -1;
    while left <= right :
        mid = math.floor((left+right)/2)
        if nums[mid] == target:
            ans = mid;
            break;
        elif nums[mid] > target:
            right = mid - 1;
        else:
            left = mid + 1;
    return ans

print(search(nums,5));

    

