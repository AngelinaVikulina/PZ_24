#Дан список размера N. Обнулить все его локальные максимумы (то есть числа,
#большие своих соседей).
A = [1, 3, 2, 4, 5, 3, 7, 6, 9]

for i in range(1, len(A)-1):
    if A[i] > A[i-1] and A[i] > A[i+1]:
        A[i] = 0

print(A)
