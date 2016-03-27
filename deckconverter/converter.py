import sqlite3
from deckconverter.logger import *

class Converter:
    """
    This class is the converter which will convert the ydk file in
    a text file in the format chosen.
    """
    def __init__(self):
        self.markdown = True
        self.cardmarket = False
        self.price = False
        self.deckFile = ""
        
    def changePriceState(self):
        self.price = not self.price
        logger.info("Price : " + str(self.price))

    def changeFormat(self):
        self.markdown = not self.markdown
        self.cardmarket = not self.cardmarket
        logger.info("Markdow : " + str(self.markdown) +
                    "   Cardmarket : " + str(self.cardmarket))

    def changeDeckFile(self, file):
        self.deckFile = file
        logger.info("Deck file: " + file)
