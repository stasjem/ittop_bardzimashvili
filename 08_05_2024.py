def calculate_product(input_list):
    result = 1
    for num in input_list:
        result *= num
    return result

my_list = [2, 3, 4, 5]
product = calculate_product(my_list)
print("Произведение элементов списка:", product)
#2
def find_min_in_list(input_list):
    if not input_list:
        return None
    return min(input_list)


my_list = [5, 3, 8, 1, 10]
result = find_min_in_list(my_list)
print("Минимум в списке:", result)
#3
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_list(lst):
    count = 0
    for num in lst:
        if is_prime(num):
            count += 1
    return count


my_list = [2, 3, 5, 6, 7, 11, 13]
result = count_primes_in_list(my_list)
print("Количество простых чисел в списке:", result)
#4
def remove_elements(lst, num):
    count = 0
    while num in lst:
        lst.remove(num)
        count += 1
    return count

my_list = [1, 2, 3, 4, 3, 5, 3]
number_to_remove = 3
removed_count = remove_elements(my_list, number_to_remove)
print("Удалено элементов:", removed_count)
print("Итоговый список:", my_list)
#5
def mary_jun(San1, san2):
    return San1 + san2

San1 = [1, 2, 3]
san2 = [4, 5, 6]

mary = mary_jun( San1,san2)
print(mary)