def bubble_sort(data):
    n = len(data)
    count = 0

    for i in range(n):
        for j in range(0, n-i-1):
            count += 1
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]

    return data, count
data = [5,2,9,1,5,6]
hasil,langkah = bubble_sort(data.copy())

print("Data: ", data)
print("Hasil: ", hasil)
print("Jumlah perbandingan: ", langkah)