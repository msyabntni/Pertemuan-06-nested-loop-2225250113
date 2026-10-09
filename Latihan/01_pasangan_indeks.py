# Loop luar untuk nilai i
# Loop dalam untuk nilai j
# count menghitung banyak pasangan

count = 0

for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
        count += 1

print(f"Banyak pasangan = {count}")