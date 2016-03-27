import sqlite3
class Converter:
    """
    This class is the converter which will convert the ydk file in
    a text file in the format chosen.
    """
    def __init__(self):
        self.markdown = True
        self.cardmarket = False
        self.price = False
        
    def changePriceState(self):
        self.price = not self.price
