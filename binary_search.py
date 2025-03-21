#print('Всё также прошу вернуть deepseek')
import time
start_time = time.time()


arr = [1,2,3,4,5,10,15,20]
target = 1
# Код бинарного поиска  
def binary_search(arr, target): 
    left, right = 0, len(arr) - 1 

    while left <= right:
        mid = (left + right) // 2 
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1

result = binary_search(arr, target)
if result != -1:
    print(f'Элемент {target} найден по индексу {result}')
else:
    print('Элемент не найден')

print((time.time() - start_time))