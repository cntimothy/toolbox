#!c:\python27\python.exe
#filename:lineobj.py

class Lineobj:
	def __init__(self, strcontent):
		self.strcontent = strcontent
		
	def tostring(self):
		return str(self.strcontent)