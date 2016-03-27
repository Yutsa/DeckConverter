import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Window(Gtk.ApplicationWindow):
    """This is the main window"""

    def __init__(self, app):
        Gtk.Window.__init__(self, title="DeckConverter",
                            application=app)
        self.set_default_size(640, 512)
