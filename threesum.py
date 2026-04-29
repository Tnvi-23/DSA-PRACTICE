def threesum(arr):
    arr.sort()
    res = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left , right = i+1 , len(arr)-1
        while left < right:
            sum = arr[i]+arr[left]+arr[right]
            if sum < 0:
                left += 1
            if sum > 0:
                right -= 1
            else:
                res.append([arr[i],arr[left],arr[right]])
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while right < left and arr[right] == arr[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return res

arr = [-1,0,1,2,-1,-4]
print(threesum(arr))