# find out lower bound of 7

import math

# finding the recent-lower or equal to targeted having their left-most index.


left = 0;

# upper bound is 5.
# lower bound is 1


def lower_bound(nums,target):
    left = 0;
    right = len(nums) - 1;
    ans = -1
    if nums[0] > target :
        return -1
    while left <= right:
        mid = math.floor((left+right)/2)
        if nums[mid] >= target:
            right = mid - 1;
            ans = mid;
        else :
            left = mid + 1;
    return ans;
    



new_ans = lower_bound([1,1,2,2,2,2,2,2,2,2,3,3,4,4,4,5,5,5,5,5,7,7,7,9],9)
print(new_ans)
        






