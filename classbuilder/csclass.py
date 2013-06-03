#!c:\python27\python.exe
#filename:csclass.py

from linefac import Linefac
from field import Field

class CsClass:
	def __init__(self, name):
		self.fieldlist = []
		self.name = name
		
	def addfield(self, field):
		self.fieldlist.append(field)
		
	def genclass(self):
		classlinelist = []
		for field in self.fieldlist:
			classlinelist = classlinelist + field.genfieldlinelist
		classlinelist.append(Linefac.genlineobj(''))
		
		for field in self.fieldlist:
			classlinelist = classlinelist + field.genproplinelist
			classlinelist.append(Linefac.genlineobj(''))
			
		return classlinelist