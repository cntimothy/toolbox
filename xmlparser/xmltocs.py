#!c:\python27\python.exe
#filename:xmltocs.xml

from table import Table
from xml.etree import ElementTree
import os

class XMLToCs:
	def __init__(self, filepath):
		self.filepath = filepath;
		self.datatables = []
		
	def transfer(self):
		doc = ElementTree.parse(self.filepath)
		root = doc.getroot()
		database = root.getchildren()
		for table in database:
			datatable = Table(table.attrib['tablename'])
			columns = table.getchildren()
			for column in columns:
				datatable.add(column.attrib['columnname'], column.attrib['columntype'],column.attrib['columnwidth'])
			self.datatables.append(datatable)
	
	def showall(self):
		for t in self.datatables:
			t.show()
			
	def writemodel(self):
		namespace = raw_input("Please input your namespace:")
		for model in self.datatables:
			if (not os.path.exists('Model')) or (os.path.isfile('Model')):
				os.makedirs('Model')
			f = file("Model\\" + model.tablenamecap + '.cs', 'w')
			try:
				self.writemodelusing(f)
				f.write('namespace ' + namespace + '\n')
				f.write('{\n')
				f.write('\tpublic class ' + model.tablename.capitalize() +'\n')
				f.write('\t{\n')
				
				for field in model.columns:
					f.write('\t\tprivate ' + field['columnfieldtype'] + ' ' + field['columnname'] + ';\n')
					
				f.write('\n')
				for field in model.columns:
					f.write('\t\tpublic ' + field['columnfieldtype'] + ' ' + field['columnnamecap'] + '\n')
					f.write('\t\t{\n')
					f.write('\t\t\tget { return ' + field['columnname'] + '; }\n')
					f.write('\t\t\tset { ' + field['columnname'] + ' = value; }\n')
					f.write('\t\t}\n')
					f.write('\n')
					
				f.write('\t}\n')
				f.write('}')
			except Exception:
				print "Some error happened while write file..."
			finally:
				f.close()
				print 'Table', model.tablename, 'is done!'
		print 'Output all done!'
		
	def writemodelusing(self, f):
		f.write('using System;\n')
		f.write('using System.Colllesections.Generic;\n')
		f.write('using System.Linq;\n')
		f.write('using System.Web;\n')
		f.write('\n')
		
	def writebllusing(self, f):
		f.write('using System;\n')
		f.write('using System.Colllesections.Generic;\n')
		f.write('using System.Linq;\n')
		f.write('using System.Web;\n')
		f.write("using System.Data;\n")
		f.write("using System.Data.SqlClient;\n")
		f.write("using DBUnity;\n")
		f.write("using Model;\n")
		f.write("using System.Text;\n")
		f.write('\n')
		
	def writebll(self):
		namespace = raw_input("Please input your namespace:")
		for model in self.datatables:
			if (not os.path.exists('BLL')) or (os.path.isfile('BLL')):
				os.makedirs('BLL')
			f = file("BLL\\" + model.tablename.capitalize() + 'BLL.cs', 'w')
			try:
				self.writebllusing(f)
				f.write('namespace ' + namespace + '\n')
				f.write('{\n')
				f.write('\tpublic class ' + model.tablenamecap + 'BLL\n')
				f.write('\t{\n')
				f.write('\t\tpublic ' + model.tablenamecap + 'BLL()\n')
				f.write('\t\t{}\n')
				f.write('\t\tstatic readonly SQLDatabase db = new SQLDatabase()\n')
				f.write('\t}\n')
				f.write('}\n')
			finally:
				f.close()
				
	def writeinsertfunc(self, f):
		f.write('\t\t\n')
		f.write('\t\t\n')
		f.write('\t\t\n')
