arr = list(map(int, input().split()))

even_count = 0
odd_count = 0

for i in arr:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
        
print(abs(even_count - odd_count))

