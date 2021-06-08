print('Kalebianka Efata Meylina Pagiling')
ini_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def nilai_pair(data):
    count = 0
    for k in range(0, len(data) - 1):
        if k % 2 != 0:
            count += 1
    return True if count >= 2 else False

evens = [2, 4, 6, 8]
print(nilai_pair(ini_list))
print(nilai_pair(evens))

