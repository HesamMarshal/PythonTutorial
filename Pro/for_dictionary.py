import time
start2 = time.perf_counter()

fruits = ["apple", "banana", "orange"]
quants = [10, 20, 8]
d = {"apple": 10, "banana": 20, "orange": 8}


# for key in d.keys():
#     print(key, d[key])

for key, val in d.items():
    print(key, val)


end2 = time.perf_counter()
print(end2 - start2)
