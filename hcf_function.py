def hcf_calculate(num1,num2):
    if num2>num1:
        z=num1
        num1=num2
        num2=z
    print(num1,num2)    
    while True:
        r=num1%num2
        num1=num2
        num2=r
        if r==0:
            return num1
            break
       

arr=[12,34,2,4,67]
arr.sort()
lowest=arr[0]
print(hcf_calculate(55,110))
