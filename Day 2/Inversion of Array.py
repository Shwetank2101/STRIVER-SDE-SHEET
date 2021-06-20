def merge(nums,temp,left,mid,right):
    i=left
    j=mid+1
    k=left
    invcount=0
    while i<=mid and j<=right:
        if nums[i]<=nums[j]:
            temp[k]=nums[i]
            i+=1
            k+=1
            
        else:
            temp[k]=nums[j]
            k+=1
            j+=1
            invcount+=(mid-i+1)
    while i<=mid:
        temp[k]=nums[i]
        k+=1
        i+=1
    while j<=right:
        temp[k]=nums[j]
        k+=1
        j+=1
    for i in range(left,right+1):
        nums[i]=temp[i]
    return invcount
            
def checkmerge(nums,temp,left,right):
    invcount=0
    if right>left:
        mid=(right+left)//2
        invcount+=checkmerge(nums,temp,left,mid)
        invcount+=checkmerge(nums,temp,mid+1,right)
        invcount+=merge(nums,temp,left,mid,right)
    return invcount

def countinversion(nums):
    n=len(nums)
    temp=[0]*n
    return checkmerge(nums,temp,0,n-1)
    
