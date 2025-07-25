
def remove_duplicate(array:list[int])->int:
    i=0
    for j in range(1,len(array)):

        if array[i]!=array[j]:
            i+=1
            array[i]=array[j]

    return i+1
#main
array = list(map(int,input().split(" ")))

k = remove_duplicate(array)

for i in range(k):
    print(array[i],end=" ")

