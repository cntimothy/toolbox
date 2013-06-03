#!c:\python27\python.exe
#filename:csclass.py

from linefac import Linefac
from field import Field
import os

class CsClass:
	def __init__(self, name):
		self.fieldlist = []
		self.name = name
		
	def addfield(self, field):
		self.fieldlist.append(field)
		
	def genclass(self):
		classlinelist = []
		classlinelist.append(Linefac.genlineobj('#region Private Field'))
		for field in self.fieldlist:
			classlinelist = classlinelist + field.genfieldlinelist()
		classlinelist.append(Linefac.genlineobj('#endregion'))
		classlinelist.append(Linefac.genlineobj(''))
		
		classlinelist.append(Linefac.genlineobj('#region Public Field'))
		for field in self.fieldlist:
			classlinelist = classlinelist + field.genproplinelist()
			classlinelist.append(Linefac.genlineobj(''))
		classlinelist.append(Linefac.genlineobj('#endregion'))
			
		return classlinelist
		