def insertion_sort(data):
    for i in range(1, len(data)):
        #value = data[i] nicht nötig
        while i > 0 and data[i-1] > data[i]:
            data[i], data[i-1] = data[i-1], data[i]
            i -= 1 #damit alle nötigen Werte bis zum kleinsten Wert vertauscht werden
    return data


def bubble_sort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data