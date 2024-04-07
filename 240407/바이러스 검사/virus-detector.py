n= int(input())
#print("n", n)

restaurant = list(map(int,input().split()))
#print("restaurant", restaurant)

headT, memT = map(int,input().split())
#print("headT ", headT, " memT ", memT)

minT = n
min_memT = 0
#print("minT", minT)
for i in range(len(restaurant)):
    cnt = 0
    restaurant[i] = restaurant[i] - headT
    if restaurant[i] > memT:
        min_memT = restaurant[i] // memT
    #print("min_memT", min_memT)
    minT += min_memT
    # print("minT", minT)
print(minT)