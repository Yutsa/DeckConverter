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
        self.convList = ""
        self.cardDB = ""
        
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

    def changeConvList(self, file):
        self.convList = file
        logger.info("Saving as: " + str(file))

    def changeCardDB(self, file):
        self.cardDB = file
        logger.info("cards.cdb : " + self.cardDB)

    def convert(self):
        print("Converting !")
        with open(self.deckFile, 'r') as ydkList:
            with open(self.convList, "w") as convertedList:
                for line in ydkList:
                    if self.markdown:
                        if "#created" in line:
                            convertedList.write("Created using " +
                                                "DeckConverter\n\n")
                        elif "#main" in line:
                            convertedList.write("\nMain Deck: \n\n")
                        elif "#extra" in line:
                            convertedList.write("\nExtra Deck: \n\n")
                        elif "!side" in line:
                            convertedList.write("\nSide Deck: \n\n")
                        else:
                            if self.price:
                                convertedList.write(line[:-1] +
                                                    "- PRICE\n")
                            else:
                                convertedList.write(line)
                    else:
                        convertedList.write("CARDMARKET -- " + line)
