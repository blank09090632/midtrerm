def bai3(a):
    sort = True
    while sort == True:
        sort = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
                sort =True
            #print(i)
            #print(a)
    return a

while True:
    n = int(input("Nhap so phan tu:"))
    if n >= 1 : 
        break
a = []
for i in range(n):
    b = int(input("Nhap phan tu:"))
    a.append(b)

print(bai3(a))