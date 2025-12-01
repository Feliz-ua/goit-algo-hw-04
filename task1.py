import random
import timeit

# ---------- 1. Алгоритм сортування злиттям (Merge Sort) ----------

def merge(left, right):
    merged = []
    Left_index =0
    Right_index =0
    
    while Left_index < len(left) and Right_index < len(right):
        if left[Left_index] <= right[Right_index]:
            merged.append(left[Left_index])
            Left_index += 1
        else:
            merged.append(right[Right_index])
            Right_index += 1
    merged.extend(left[Left_index:])
    merged.extend(right[Right_index:])
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# --- 2. Алгоритм сортування вставками (Insertion Sort) ---
def insertion_sort(lst):
    lst = list(lst)  # щоб не псувати вхідний список
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


# ---------- 3. Обгортка над вбудованим Timsort ----------

def timsort_sort(lst):
    return sorted(lst)

# ---------- Генерація тестових даних ----------

def generate_random_list(n):
    return [random.randint(0, 10_000_000) for _ in range(n)]

def generate_sorted_list(n):
    return list(range(n))

def generate_reversed_list(n):
    return list(range(n, 0, -1))


# ---------- Функція для заміру часу ----------

def measure_time(func, data, number=5):
    return timeit.timeit(lambda: func(data), number=number)


def main():
    sizes = [1_000, 5_000, 10_000]  # можна збільшувати за потреби

    for n in sizes:
        print(f"\nРозмір масиву: {n}")

        random_data = generate_random_list(n)
        sorted_data = generate_sorted_list(n)
        reversed_data = generate_reversed_list(n)
      

        for data_name, data in [
            ("випадкові", random_data),
            ("вже відсортовані", sorted_data),
            ("обернено відсортовані", reversed_data),
        ]:
            print(f"\n  Дані: {data_name}")

            t_merge = measure_time(merge_sort, data)
            t_insert = measure_time(insertion_sort, data)
            t_timsort = measure_time(timsort_sort, data)

            print(f"    merge_sort:    {t_merge:.6f} c")
            print(f"    insertion_sort:{t_insert:.6f} c")
            print(f"    Timsort:       {t_timsort:.6f} c")


if __name__ == "__main__":
    main()
