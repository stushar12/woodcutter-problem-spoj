import  sys

n=int(input("Enter number of trees "))
y=int(input("Enter the amount of wood you want to cut "))
arr=[]
print("Enter height of trees :")
for i in range(0,n):
    z=int(input())
    arr.append(z)

arr.sort()
sum=0

for i in range(0,n):
        sum=sum+arr[i]

def check(mid):
    height=0
    for i in range(0,n):
            if(arr[i]<mid):
                continue
            else:
                height=height+(arr[i]-mid)
    if(height>=y):
        return height
    else:
        return 0


def binarySearch():
    if (sum < y):
      return -1
    lower=arr[0]
    upper=arr[n-1]
    min=sys.maxsize
    while lower <= upper: 
  
        mid = lower + ( (upper-lower) // 2); 
        a=check(mid)
        if (a):
            c=a-y
            if(c<min):
                min=c
                minimum=mid
            lower=mid+1
        else: 
            upper=upper-1
    return minimum

p=binarySearch()
if (p==-1):
    print("Not Possible")
else:
    print(f"Minimum height is {p} which should be kept to collect {y} amount of wood ")
