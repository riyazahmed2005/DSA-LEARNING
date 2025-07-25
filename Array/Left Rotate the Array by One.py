def rotateLeft(array)->list[int]:
    l=len(array)-1
    temp=array[0]
    for i in range(l):
        array[i]=array[i+1]
    array[l]=temp
    return array



#main

array = list(map(int,input().split(" ")))
print(rotateLeft(array))