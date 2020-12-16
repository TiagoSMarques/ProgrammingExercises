
data = input("Enter matrix size: ")
[y, x] = [int(n) for n in data.split(',')]


matrix = [[0 for i in range(x)] for j in range(y)]


for i in range(y):
    for j in range(x):
        matrix[i][j] = i*j

print(matrix)
