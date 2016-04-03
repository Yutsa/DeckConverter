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
        self.cursor = None
        self.original_decklist = None
        
    def changePriceState(self):
        """ Enables or disables the price feature."""
        self.price = not self.price
        logger.info("Price : " + str(self.price))

    def changeFormat(self):
        """Changes the convertion format"""
        self.markdown = not self.markdown
        self.cardmarket = not self.cardmarket
        logger.info("Markdow : " + str(self.markdown) +
                    "   Cardmarket : " + str(self.cardmarket))

    def changeDeckFile(self, file):
        """Changes the deck file"""
        self.deckFile = file
        logger.info("Deck file: " + file)

    def changeConvList(self, file):
        """Changes the converted list file"""
        self.convList = file
        logger.info("Saving as: " + str(file))

    def changeCardDB(self, file):
        """"Changes the card database"""
        self.cardDB = file
        logger.info("cards.cdb : " + self.cardDB)

    def hashtagLine(self, line):
        """Handles the conversion of meta lines starting with a #
        or !"""
        if "#created" in line:
            return("Created using DeckConverter\n\n")
        elif "#main" in line:
            return("\n**Main Deck:** \n\n")
        elif "#extra" in line:
            return("\n**Extra Deck:** \n\n")
        elif "!side" in line:
            return("\n**Side Deck:** \n\n")
        else:
            return(line)

    def connectDB(self):
        """Connects to the database"""
        conn = sqlite3.connect(self.cardDB)
        self.cursor = conn.cursor()
        logger.info("Connected to the database.")

    def getCardName(self, id):
        """Gets the card name using its ID"""
        id_req = (id,)
        for row in self.cursor.execute('SELECT name FROM texts WHERE id=?', id_req):
            return(row[0] + '\n')

    def getCardCopies(self, card):
        """Returns the number of copy of the same card"""
        count = 1
        nb_card = self.original_decklist.count(card)
        for i in range(0, nb_card - 1):
            self.original_decklist.remove(card)
        return nb_card
        
    def convertToMarkdown(self, sourceList, destList):
        """Converts the decklist to markdown"""
        self.original_decklist = sourceList.readlines()
        for line in self.original_decklist:
            if "#" in line or "!" in line:
                destList.write(self.hashtagLine(line))
            else:
                destList.write("* " + str(self.getCardCopies(line))
                               + " " + self.getCardName(line[:-1]))
        
    def convert(self):
        self.connectDB()
        print("Converting !")
        with open(self.deckFile, 'r') as ydkList:
            with open(self.convList, "w") as convertedList:
                if self.markdown:
                    self.convertToMarkdown(ydkList, convertedList)
                else:
                    convertedList.write("CARDMARKET -- " + line)
