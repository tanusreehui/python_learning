x=list()
print("Enter the value")
for i in range(0,3):
    a=int(input("Enter the number  "))
    x.append(a)
print(x)
x.sort(reverse=True)
print(x)
ans=1
p=1
i=0
while True:
    if x[i]%p==0 && x[i+1]%p==0 :
        print("test")
    p=p+1