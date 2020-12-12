arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def printThirds(arr):
    if (len(arr)-1) % 3 == 0:
        print(arr[0])
    if len(arr) > 1:
        printThirds(arr[1:])
printThirds(arr)