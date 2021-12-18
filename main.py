import math
list1=[]
n = int(input("Enter number of elements : "))
print("Enter the x value :")
for i in range(n):
    x=float(input())
    list1.append(x)
list2=[]
print("Enter the y value :")
for i in range(n):
        y = float(input())
        list2.append(y)
list3=[]
print("Enter the z value :")
for i in range(n):
        z = float(input())
        list3.append(z)
sx=sum(list1)
sy=sum(list2)
sz=sum(list3)
sxe=0
sye=0
sze=0
for i in range(n):
    sxe=sxe+pow(list1[i],2)
for i in range(n):
    sye=sye+pow(list2[i],2)
for i in range(n):
    sze=sze+pow(list3[i],2)
sxz=0
for i in range(n):
    sxz=sxz+list1[i]*list3[i]
sxy=0
for i in range(n):
    sxy=sxy+list1[i]*list2[i]
syz=0
for i in range(n):
    syz=syz+list2[i]*list3[i]
print("sum of x is :",sx)
print("sum of y is :",sy)
print("sum of z is :",sz)
print("x square is :",sxe)
print("y square is :",sye)
print("z square is :",sze)
print("sum of xz is :",sxz)
print("sum of xy is :",sxy)
print("sum of yz is :",syz)