from fibonacci import fibonacci
from sum_lists import sum_lists
from calculate import calculate, square, cube
from my_decoration import my_tax_decorator

# fibonacci
for x in fibonacci(5, 20):
    print(x)

# sum_lists
print(list(sum_lists([1,2,3], [4,5])))

# calculate
print(list(calculate([1,2,3], cube)))

# decorator
@my_tax_decorator
def get_report():
    return {"income": 1000, "tax": 200}

print(get_report())