def hcf_calculate(num,arr):
    
    for i in arr:
           r=i%num
           if r!=0:
                return False
    return True


arr=[12,48,16,24]
arr.sort()
lowest=arr[0]
x=lowest
while True:
    if(hcf_calculate(x,arr)):
        print(x)
        break
    x=x-1


