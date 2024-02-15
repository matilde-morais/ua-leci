def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontrar o índice do menor elemento restante
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Trocar o menor elemento com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso
my_list = [5, 2, 9, 1, 5]
selection_sort(my_list)
print("Lista ordenada:", my_list)