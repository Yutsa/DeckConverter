#!/usr/bin/python3
import sys
from deckconverter.application import Application

app = Application()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
