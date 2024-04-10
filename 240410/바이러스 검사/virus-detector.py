n= int(input())
arr = list(map(int, input().split()))
test = list(map(int, input().split()))
#print(n, arr, test)

test_min = 0

for i in range(n):
    arr[i] -= test[0]
    test_min += 1
#print(test_min)

for j in range(n):
    if arr[j] >= test[1]:
        test_min += arr[j] // test[1]
        arr[j] = arr[j] % test[1]
    if arr[j] > 0:
        test_min += 1
print(test_min)