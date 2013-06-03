#!c:\python27\python.exe
#filename:field.py

from linefac import Linefac
from lineobj import Lineobj

class Field:
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.property = name[0].upper() + name[1:]
	
	def genfieldlinelist(self):
		fieldlinelist = []
		fieldlinelist.append(Linefac.genlineobj('private ' + self.type + ' ' + self.name + ';'))
		return fieldlinelist;
		
	def genproplinelist(self):
		proplinelist = []
		proplinelist.append(Linefac.genlineobj('public ' + self.type + ' ' + self.property))
		proplinelist.append(Linefac.genlineobj('{'))
		proplinelist.append(Linefac.genlineobj('get { return ' + self.name + '; }'))
		proplinelist.append(Linefac.genlineobj('set { ' + self.name + ' = value; }'))
		proplinelist.append(Linefac.genlineobj('{'))
		return proplinelist