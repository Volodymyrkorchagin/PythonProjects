def square(x):
    return x * x

def cube(x):
    return x * x * x

def calculate(list, function_to_call):
    for item in list:
        result = function_to_call(item)
        yield result
