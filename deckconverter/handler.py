from deckconverter.converter import Converter
from gi.repository import Gtk
from deckconverter.logger import *

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

    def onClickConvert(self, convertButton):
        self.converter.convert()

    def onClickCdb(self, cdbChooser):
        self.converter.changeCardDB(cdbChooser.get_filename())

    def onClickSaveAs(self, window):
        dialog = Gtk.FileChooserDialog("Save as", window,
                                       Gtk.FileChooserAction.SAVE,
                                       (Gtk.STOCK_CANCEL,
                                        Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OK,
                                        Gtk.ResponseType.OK))

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.converter.changeConvList(dialog.get_filename())
        else:
            logger.info("Canceled the selection of the saving file.")

        dialog.destroy()
