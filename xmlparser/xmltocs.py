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
			f = file("Model\\" + model.tablename.capitalize() + '.cs', 'w')
			try:
				f.write('using System;\n')
				f.write('using System.Colllesections.Generic;\n')
				f.write('using System.Linq;\n')
				f.write('using System.Web;\n')
				f.write('\n')
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
			finally:
				f.close()
				print 'Table', model.tablename, 'is done!'
		print 'Output all done!'