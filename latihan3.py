#Raka Emillul Fata
#Latihan 3 : Implementasi Insertion Sort

def insertion_sort(data):
    count = 0

    for i in range(1, len(data)):
        key = data[i]
        j=i-1

        while j>=0 and data[j]>key:
            count += 1
            data[j+1]=data[j]
            j-=1

        
        data[j+1]=key

    return data, count

data           = [5,2,9,1,5,6]
hasil, langkah = insertion_sort(data.copy())

#Output (O)
print("Data: ", data)
print("Hasil: ", hasil)
print("Jumlah Perbandingan: ", langkah)