array = list(map(int,input().split(" ")))

maximum=array[0]

secound_maximum=float("-inf")

for i in array:
    if i>=maximum:
        secound_maximum=maximum
        maximum=i
    elif i>secound_maximum and i!=maximum:
        secound_maximum=i
print(secound_maximum)