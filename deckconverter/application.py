from gi.repository import Gtk
from deckconverter.window import Window
from deckconverter.handler import Handler

class Application(Gtk.Application):
    """
    This is the application itsel. It creates the window and begins
    the event loop.
    """
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("deckconverter/window.glade")
        self.win = self.builder.get_object("main_window")
        self.add_window(self.win)

        self.builder.connect_signals(Handler())
        self.win.show_all()
        

    def do_startup(self):
        Gtk.Application.do_startup(self)
