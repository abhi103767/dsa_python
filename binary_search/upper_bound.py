


def upper_bound(nums,target) :
    left = 0;
    right = len(nums) - 1;
    while left <= right:
        mid = math.floor((left+right) / 2)
        if nums[mid] > target:
             ans = mid;
        else:
            
        
        
