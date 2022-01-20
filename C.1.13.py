print('Kalebianka Efata Meylina Pagiling')
ini_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

def reverse(data):
    temp = []
    n = len(data) - 1
    for thing in range(n, -1, -1):
        temp.append(data[thing])
    return temp

print(ini_list)
print(reverse(ini_list))
