#Программа для линейного поиска
arr = [1,2,3,4,5,10,15,20, 22, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 40, 41, 42]
target = 100 

# Код линейного поиска  
def linear_search(arr, target):
    for index, value in enumerate(arr): # цикл проверяет каждый аргумент списка сравнивая его с 'target' с помощью функции enumerate 
        if value == target:
            return index
    return -1
result = linear_search(arr,target)
if result != -1:
    print(f'Элемент {target} найден по индексу {result}.') 
else:
    print(f'Элемент {target} не найден в списке.')

