#!c:\python27\python.exe
#filename:doc.py

class Doc:
	def __init__(self):
		self.tabNo = 0
		self.lines = []
		
	def append(self, lineobj):
		self.lines.append(lineobj)
		
	def writeall(self, file):
		for line in self.lines:
			if line.tostring() == '}':
				self.tabNo = self.tabNo - 1
			tablist = ['\t']*self.tabNo
			str = ''.join(tablist) + line.tostring()
			file.write(str + '\n')
			if line.tostring() == '{':
				self.tabNo = self.tabNo + 1
				
	def clear(self):
		self.lines = []