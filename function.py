def is_divisible(num,arr):
    for i in arr:
        r=num % i
        if r!=0:
            return False
    return True



print("Press 0 to exit")
arr=list()
while True:
    a=int(input("Enter the value  :"))
    if a==0:
        break
    arr.append(a)
arr.sort()
print("The elements are :",arr)
highest=arr[-1]
i=1
while True:
    if is_divisible(highest*i,arr):
        print(highest*i)
        break
    i=i+1

