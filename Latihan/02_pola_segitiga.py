# Loop luar menentukan baris
# Loop dalam menentukan jumlah simbol pada setiap baris

n = int(input("n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()