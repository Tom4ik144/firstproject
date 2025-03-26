#Программа для бинарного поиска
arr = [1,2,3,4,5,10,15,20, 22, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 40, 41, 42]
target = 33
# Код бинарного поиска  
def binary_search(arr, target): 
    left, right = 0, len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid              #элемент найден в середине, возвращаем индекс
        elif arr[mid] < target:
            left = mid + 1          #элемент ищем в левой половине
        else:
            right = mid -1          #элемент ищем в левой половине

result = binary_search(arr, target)
if result != -1:
    print(f'Элемент {target} найден по индексу {result}')
else:
    print('Элемент не найден')
