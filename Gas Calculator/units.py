class rateUnit:
    """Contains the type of unit for the rate"""
    def __init__(self):
        self.type = "mpg"
        self.other = "kpl"
    
    def switch(self):
        if (self.type == "mpg"):
            self.type = "kpl"
            self.other = "mpg"
        else:
            self.type = "mpg"
            self.other = "kpl"

class distanceUnit:
    """Contains the type of unit for the distance"""
    def __init__(self):
        self.type = "km"
        self.other = "mi"

    def switch(self):
        if (self.type == "km"):
            self.type = "mi"
            self.other = "km"
        else:
            self.type = "km"
            self.other = "mi"

class priceUnit:
    """Contains the type of unity for the price"""
    def __init__(self):
        self.type = "L"
        self.other = "gal"

    def switch(self):
        if (self.type == "L"):
            self.type = "gal"
            self.other = "L"
        else:
            self.type = "L"
            self.other = "gal"