import random
import time

def generate_random_matrix(m, n, min_limit, max_limit):
    matrix = [[random.randint(min_limit, max_limit) for j in range(n)] for i in range(m)]
    return matrix
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


user_m = int(input("Введите количество строк (m): "))
user_n = int(input("Введите количество столбцов (n): "))
user_min_limit = int(input("Введите минимальное значение: "))
user_max_limit = int(input("Введите максимальное значение: "))

random_matrix = generate_random_matrix(user_m, user_n, user_min_limit, user_max_limit)

# Сортировка строк матрицы с помощью сортировки выбором
start_time = time.time()
for row in random_matrix:
    selection_sort(row)
selection_sort_time = time.time() - start_time
print("Время работы сортировки выбором: {:.6f} секунд".format(selection_sort_time))
# Сравнение с встроенной функцией сортировки
start_time = time.time()
for row in random_matrix:
    row.sort()
print("Встроенная сортировка заняла: {:.4f} секунд".format(time.time() - start_time))


