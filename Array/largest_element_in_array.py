array = list(map(int,input().split(" ")))
def maximum(array)-> int:

    maximum=array[0]

    for i in array:
        if i >maximum:
            maximum = i
    return maximum
print(maximum(array))
