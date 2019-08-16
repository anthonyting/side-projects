def rate(num, unit):
    """Takes number, unit, returns L/km"""
    if (unit == "mpg"):
        # US gallon
        num = 3.785412/(num * 1.609344)
    elif (unit == "kpl"):
        num = 1/num
    else:
        raise "Invalid Units."

    print(f"rate: {num}")
    return num

def distance(num, unit):
    """Takes number, distance unit, returns km"""
    if (unit == "km"):
        pass
    elif (unit == "mi"):
        num = num * 1.609344
    else:
        raise "Invalid Unit. Only accept 'km' or 'mi'."
    print(f"distance: {num}")
    return num

def price(num, unit):
    """Takes number, volume unit, returns price in $/l"""
    if (unit == 'L'):
        num = num / 100
    elif (unit == "gal"):
        num = num / 3.785412 / 100
    else:
        raise "Invalid Unit. Only accept 'l' or 'gal'."
    print(f"price: {num}")
    return num

def calculate(rate, distance, price):
    """rate in litres/km
    distance in km
    price in $/litre"""
    return rate * distance * price