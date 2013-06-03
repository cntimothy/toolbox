#!c:\python27\python.exe
#filename:field.py

from linefac import Linefac
from lneobj import Lineobj

class Field:
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.property = name[0].upper() + name[1:]
	
	def tostring(self):
		return 'private ' + type + ' ' + name + ';'
		
	def toproperty(self):
		return 'public ' + type + ' ' + property + '\n'