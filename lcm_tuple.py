def hcf_calculation(num,arr):
    for x in arr:
       
        r=num%x
        if r!=0:
            return False
            break

    return True

arr=(2,4,6,12,10,8)
heighest=max(arr)

i=1
while True:
    if(hcf_calculation(heighest*i,arr)):
        print(heighest*i)
        break
    i=i+1
