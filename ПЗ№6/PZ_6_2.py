#Дан список A размера N и целые числа K и L (1 < K < L < N). Переставить в обратном
#порядке элементы списка, расположенные между элементами AK и AL, включая эти
#элементы.
A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
K = 2
L = 7


A[K-1:L] = A[K-1:L][::-1]

print(A)
