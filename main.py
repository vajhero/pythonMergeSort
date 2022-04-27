from traceback import print_stack

file = open("numbers.txt", "r+")


def mergeSort(list):
    listLength = len(list)
    if listLength > 1:
        midPoint = listLength//2
        left = list[:midPoint]
        right = list[midPoint:]

        mergeSort(left)
        mergeSort(right)

        leftLength = len(left)
        rightLength = len(right)

        i = j = k = 0
        while i < leftLength and j < rightLength:
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        while i < leftLength:
            list[k] = left[i]
            i += 1
            k += 1

        while j < rightLength:
            list[k] = right[j]
            j += 1
            k += 1


def printList(list):
    for i in range(len(list)):
        print(list[i])
    print()


list = [line.rstrip() for line in file]

print(list)

print("Lista:")
print("")
printList(list)
mergeSort(list)

print("Posortowana lista:")
print()
printList(list)

listStr = ', '.join(str(v) for v in list)
file.write("\nPosortowana lista: " + listStr)
file.close()
