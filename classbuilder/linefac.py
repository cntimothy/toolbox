#!c:\python27\python.exe
#filename:linefac.py

from lineobj import Lineobj

class Linefac:
	@staticmethod
	def genlineobj(str):
		return Lineobj(str)