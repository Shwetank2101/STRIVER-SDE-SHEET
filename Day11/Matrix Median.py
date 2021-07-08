def search(nums,low,high):
    if low>high:
        return
    if low==high:
        return nums[low]
    mid=(high-low+1)
l=list(map(int,input().split()))
