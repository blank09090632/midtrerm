import math
def bai1(n):
    b = "la so nghuyen to"
    a = "khong phai so nguyen to"
    if n == 1: 
        print(n, b)
        return
    if n % 2 == 0: 
        print(n, b)
        return
    for i in range(3,round(math.sqrt(n))+1,2):
        if n % i == 0: 
            print(n,a)
            return
    print(n,b)
while True:
    n = int(input("Nhap so:"))
    if n >= 1 : break
bai1(n)