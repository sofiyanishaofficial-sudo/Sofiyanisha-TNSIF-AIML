arr = [10, 20, 30, 40, 50]

reverse_arr = []

for i in range(len(arr) - 1, -1, -1):
    reverse_arr.append(arr[i])

print(reverse_arr)
