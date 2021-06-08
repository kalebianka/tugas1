print('Kalebianka Efata Meylina Pagiling')
from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data = [3, 4, 6, 9, 5, 4]
print(areDistinct(data))
