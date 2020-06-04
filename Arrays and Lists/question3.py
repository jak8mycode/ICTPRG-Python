values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45, 78]

sum_values = 0
avg_values = 0
max_values = max(values)

for val in values:
    sum_values += val

avg_values = sum_values / len(values)

print(sum_values)
print(avg_values)
print(max_values)