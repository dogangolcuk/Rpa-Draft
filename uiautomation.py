# encoding: utf-8

from pywinauto_recorder.player import *


with UIPath(u"||List"):
	double_click(u"test6||ListItem")

with UIPath(u"test6||Window"):
	with UIPath(u"||Pane"):
		click(u"||AppBar->View||Button")
	click(u"||Pane->Pop-up||Window->||Menu->Large icons||MenuItem->Large icons||Text")
	click(u"||Pane")
