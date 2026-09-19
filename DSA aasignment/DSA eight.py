arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_sum = arr[0]
current_sum = arr[0]

start = 0
best_start = 0
best_end = 0

for i in range(1, len(arr)):
    if current_sum + arr[i] < arr[i]:
        current_sum = arr[i]
        start = i
    else:
        current_sum += arr[i]

    if current_sum > max_sum:
        max_sum = current_sum
        best_start = start
        best_end = i

subarray = arr[best_start:best_end + 1]

print("Maximum Subarray Sum:", max_sum)
print("Subarray:", subarray)
