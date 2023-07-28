def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def binary_search(element, arr):
    first = 0
    last = len(arr) - 1
    resultOK = False
    result = None
    while first < last:
        mid = (first + last) // 2

        if arr[mid] == element:
            first = last = mid
            resultOK = True
            result = mid
            break
        elif arr[mid] < element:
            first = mid + 1
        else:
            last = mid - 1

    if resultOK:
        print(f"Элемент найден на позиции {result}.")
    else:
        print("Элемент не найден.")

    print("Конец")


if __name__ == "__main__":
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    element_to_search = 22

    # Сортировка методом пузырька
    sorted_list = bubble_sort(unsorted_list.copy())
    print("Отсортированный список:", sorted_list)

    # Двоичный поиск
    result_index = binary_search(element_to_search, sorted_list)