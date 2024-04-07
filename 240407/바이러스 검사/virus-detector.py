n= int(input())

restaurant = list(map(int,input().split()))

headT, memT = map(int,input().split())

minT = n
min_memT = 0
for i in range(len(restaurant)):
    cnt = 0
    restaurant[i] -= headT
    if restaurant[i] > 0:
        min_memT = restaurant[i] // memT
    minT += min_memT + 1