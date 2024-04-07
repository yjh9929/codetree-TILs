n= int(input())

restaurant = list(map(int,input().split()))

headTmax, memTmax = map(int,input().split())

minT = n
min_memT = 0
for i in range(len(restaurant)):
    restaurant[i] -= headTmax
    if restaurant[i] == 0:
        continue
    else:
        minT += restaurant[i] // memTmax
        if restaurant[i] % memTmax != 0:
            minT += 1
print(minT)