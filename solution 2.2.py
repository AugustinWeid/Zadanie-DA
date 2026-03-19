"""
Реализовать функцию (или тело функции), которая находит единственное 
отсутствующее число из последовательности натуральных чисел 1,2,…,n.
# Пример:
nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11]
print(missing_number(nums))
# Вывод: 
7
Оценить оптимальность решения по времени и памяти и прикрепить текст кода.
"""
def missing_number(nums):
    if not nums:
        return 1
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def missing_number_xor(nums):
    if not nums:
        return 1
    n = len(nums) + 1
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
    for num in nums:
        xor_all ^= num
    return xor_all

if __name__ == "__main__":
    input_str = input("Введите последовательность чисел через пробел: ").strip()
    if not input_str:
        print("Вы ввели пустую последовательность")
    else:
        nums = list(map(int, input_str.split()))
        result = missing_number(nums)
        print(f"Пропущенное число: {result}")
        # Проверка XOR
        result_xor = missing_number_xor(nums)
        print(f"Проверка XOR: {result_xor}")
"""
Так как в задании указано, что надо чтобы выделили единственное число,
 программа рассчитана именно на это
"""
