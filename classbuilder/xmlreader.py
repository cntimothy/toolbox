#!c:\python27\python.exe
#filename:xmlreader.py

from xml.etree import ElementTree

class XmlReader:
	def __init__(self):
		self.classes = []
		
	def read(self):
		doc = ElementTree.parse("test.xml")
		root = doc.getroot()
	
		children = root.getchildren()
		