# Combine two dictionaries using ChainMap.
from collections import ChainMap

dict1 = {
    "address": "etiene", "age": 12
}
dict2 = {
    "name": "etiene", "age": 14
}

combination = ChainMap(dict1, dict2)
print(combination)