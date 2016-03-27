from deckconverter.converter import Converter

class Handler:
    """
    This is the handler for the signals emitted by the application.
    """
    def __init__(self):
        self.converter = Converter()
        
    def onFileChosen(self, fileChooser):
        self.converter.changeDeckFile(fileChooser.get_filename())
        
    def onClickPrice(self, priceButton):
        self.converter.changePriceState()

    def onClickFormat(self, formatButton):
        self.converter.changeFormat()
