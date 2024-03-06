import json
from path import path_to_count_json


def readDict():
    with open(path_to_count_json) as f:
        return json.load(f)


def writeDict(obj):
    with open(path_to_count_json, 'wt') as f:
        json.dump(obj, f)


sample = dict(name='fred', age=31, grades=[1, 34, 55])

# test the function
writeDict(sample)

# test the function
somedict = readDict()
print(somedict)
