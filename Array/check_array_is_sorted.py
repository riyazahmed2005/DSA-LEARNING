array = list(map(int,input().split(" ")))

def isSorted(array)->bool:

    for i in range(len(array)-1):
        if array[i]<=array[i+1]:
            continue
        else:
            return False
    return True
print(isSorted(array))

