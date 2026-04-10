r = int(input("Rows: "))
c = int(input("Columns: "))

A = []
B = []
C = []

print("Enter matrix A:")
for i in range(r):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter matrix B:")
for i in range(r):
    row = list(map(int, input().split()))
    B.append(row)

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Sum matrix:")
for i in C:
    print(i)