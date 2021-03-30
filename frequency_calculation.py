def frequency_calculation(num,arr):
    count=0
    for i in arr:
        if num==i:
            count=count+1
    return count


arr=[12,2,3,4,5,3,2,5,6,7,89,44,3,4,5,67,4,5,3,3,2,2,12]
arr.sort()
print(arr)
i=0
while True:
    c=frequency_calculation(arr[i],arr[i:])
    print(arr[i],c)
    i=i+c
    if i==len(arr):
        break

