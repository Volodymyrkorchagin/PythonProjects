def get_report(data):
    return {"income": 1000, "tax": 200}

def my_tax_decorator(func):
    def wrapper():
        data = func()
        new_data = {}
        for key, value in data.items():
            if key == "income":
                new_key = "Income"
            elif key == "tax":
                new_key = "Tax"

            new_data[new_key] = value
        return new_data
    return wrapper
