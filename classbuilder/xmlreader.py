#!c:\python27\python.exe
#filename:xmlreader.py

from xml.etree import ElementTree
from field import Field
from csclass import CsClass

class XmlReader:
	def __init__(self):
		self.classes = []
		
	def read(self):
		doc = ElementTree.parse("test.xml")
		root = doc.getroot()
	
		childrenofroot = root.getchildren()
		for child in childrenofroot:
			csclass = CsClass(child.attrib['name'])
			grandsons = child.getchildren()
			for grandson in grandsons:
				field = Field(grandson.attrib['name'], grandson.attrib['type'])
				csclass.addfield(field)
			self.classes.append(csclass)
		return self.classes