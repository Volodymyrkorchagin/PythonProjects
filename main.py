tuple1 = (1, 2, 30, 4, 5)
tuple2 = (10, 2, 30, 1, 50)
tuple3 = (-1, 2, 30, -4, 1)

common = set(tuple1) & set(tuple2) & set(tuple3)

print("General elements:", common)

unique1 = set(tuple1) - set(tuple2) - set(tuple3)
unique2 = set(tuple2) - set(tuple1) - set(tuple3)
unique3 = set(tuple3) - set(tuple1) - set(tuple2)

print("Unique for tuple1:", unique1)
print("Unique for tuple2:", unique2)
print("Unique for tuple3:", unique3)

somePosition = []

for item in range(len(tuple1)):
    if(tuple1[item] == tuple2[item] == tuple3[item]):
        somePosition.append(tuple1[item])

print("Elements in the same positions: ",somePosition)
