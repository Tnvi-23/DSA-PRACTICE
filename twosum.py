def twosum(target,arr):
    seen = {}
    for i,num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        seen[num]=i

arr = [3,2,4]
print(twosum(6,arr))