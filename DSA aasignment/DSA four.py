arr = [10, 20, 10, 30, 20, 40, 30]

new_arr = []

for num in arr:
    if num not in new_arr:
        new_arr.append(num)

print(new_arr)
