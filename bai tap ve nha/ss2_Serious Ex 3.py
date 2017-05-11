
s = int(input(" Nhap so * ban muon in "))
xs = int(input(" Nhap so xs ban muon in "))
print("*" * s)

print("x*" * xs)

print()

n = int(input(" Nhap so hang can in: "))
m = int(input(" Nhap so cot can in: "))
for i in range(n):
    if i % 2 == 0:
        print("x * " * m)
    else:
        print("* X " * m)

