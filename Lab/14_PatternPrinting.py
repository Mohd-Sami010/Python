n = 5
# Right angle triangle
for i in range(1, n+1):
    print("*" * i)
# Equilateral triangle
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
# Diamond
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1))
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*"*(2*i-1))