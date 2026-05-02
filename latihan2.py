#Raka Emillul Fata
#Latihan 2 : Implementasi Selection Sort

def selection_sort(data):
    n = len(data)
    count = 0

    for i in range  (n):
        min_index = i
        for j in range(i+1,n):
            count += 1
            if data[j] < data[min_index]:
                min_index = j

        data[i],data[min_index]=data[min_index],data[i]
    return data, count

data           = [5,2,9,1,5,6]
hasil, langkah = selection_sort(data.copy())

#Output (O)
print("Data: ", data)
print("Hasil: ", hasil)
print("Jumlah Perbandingan: ", langkah)
