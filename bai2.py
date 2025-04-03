def bai2(n):
    if n == 0: return 1
    a = 1
    for i in range(0,n):
        a = a*(n-i)
    return a

while True:
    n = int(input("Nhap so:"))
    if n >= 0 : break
print(bai2(n))