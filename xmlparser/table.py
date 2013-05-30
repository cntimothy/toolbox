#!c:\python27\python.exe
#filename:table.py
stringlist = ['char', 'varchar', 'nvarchar']
intlist = ['int']
sqldbtypedic = {'char':'Char', 'varchar':'VarChar', 'nvarchar':'NVarChar', 'int':'Int'}
nettypedic = {'char':'string', 'varchar':'string', 'nvarchar':'string', 'int':'int'}
class Table:
	def __init__(self, tablename):
		self.columns = []
		self.columnnamelist = []
		self.tablename = tablename
		self.tablenamecap = tablename[0].upper() + tablename[1:]
		
	def add(self, columnname, columntype, columnwidth):
		column = {}
		column['columnname'] = columnname
		column['columntype'] = columntype
		column['columnwidth'] = columnwidth
		column['columnnamecap'] = columnname[0].upper() + columnname[1:];
		column['columnnettype'] = nettypedic[columntype]
		column['columnsqldbtype'] = sqldbtypedic[columntype]
		if columnwidth == 'max':
			column['columnsqldbwidth'] = 'int.MaxValue'
		else:
			column['columnsqldbwidth'] = columnwidth
		self.columns.append(column)
		self.columnnamelist.append(columnname)
		
	def show(self):
		print 'Table\'s name:', self.tablename
		for singlecolumn in self.columns:
			for (k, v) in singlecolumn.items():
				print 'dict[%s]' % k, " : ", v