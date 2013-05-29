#!c:\python27\python.exe
#filename:table.py
stringlist = ['char', 'varchar', 'nvarchar']
intlist = ['int']
class Table:
	def __init__(self, tablename):
		self.columns = []
		self.tablename = tablename
		self.tablenamecap = tablename[0].upper() + tablename[1:]
		
	def add(self, columnname, columntype, columnwidth):
		column = {}
		column['columnname'] = columnname
		column['columntype'] = columntype
		column['columnwidth'] = columnwidth
		column['columnnamecap'] = columnname[0].upper() + columnname[1:];
		if columntype in stringlist:
			column['columnfieldtype'] = 'string'
		elif columntype in intlist:
			column['columnfieldtype'] = 'int'
		self.columns.append(column)
		
	def show(self):
		print 'Table\'s name:', self.tablename
		for singlecolumn in self.columns:
			for (k, v) in singlecolumn.items():
				print 'dict[%s]' % k, " : ", v