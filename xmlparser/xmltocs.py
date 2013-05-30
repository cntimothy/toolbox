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
			f = file("BLL\\" + model.tablenamecap + 'BLL.cs', 'w')
			try:
				self.writebllusing(f)
				self.writeline(f, 0, 'namespace ' + namespace)
				self.writeline(f, 0, '{')
				self.writeline(f, 1, 'public class ' + model.tablenamecap + 'BLL()')
				self.writeline(f, 1, '{')
				self.writeline(f, 2, 'public ' + model.tablenamecap + '(){}')
				self.writeline(f, 2, '')
				self.writeline(f, 2, 'static readonly SQLDatabase db = new SQLDatabase();')
				self.writeline(f, 2, '')
				self.writeinsert(f, model)
				self.writeline(f, 1, '}')
				self.writeline(f, 0, '}')
			finally:
				f.close()
				
	def writeline(self, f, tabNo, strcontent):
		tablist = ['\t']*tabNo
		tabstr = ''.join(tablist)
		f.write(tabstr + strcontent + '\n')
		
	def writeinsert(self, f, model):
		self.writeline(f, 2, 'public static bool Insert(List<' + model.tablenamecap + '> models, ref string e)')
		self.writeline(f, 2, '{')
		self.writeline(f, 3, 'int count = models.Count;')
		self.writeline(f, 3, 'for(int i = 0; i < count; i++)')
		self.writeline(f, 3, '{')
		#make sql statement
		strsql = 'insert into sb_' + model.tablenamecap + '('
		strsql += ','.join(model.columnnamelist) + ')'
		strsql += 'values(@'
		strsql += ",@".join(model.columnnamelist) + ')'
		self.writeline(f, 4, 'string sql = \"' + strsql + '\";')
		
		self.writeline(f, 4, 'SqlParameter[] pamaters = ')
		self.writeline(f, 4, '{')
		
		templist = []
		for col in model.columns:			
			templist.append('new SqlParameter(\"@' + col['columnname'] + '\", SqlDbType.' + col['columnsqldbtype'] + ', ' + col['columnsqldbwidth'] + ')')
		tempstr = ',\n\t\t\t\t'.join(templist)
		self.writeline(f, 4, tempstr)
		self.writeline(f, 4, '}')
		
		tempcount = 0
		for col in model.columns:
			self.writeline(f, 4, 'parameters[' + str(tempcount) + '].Value = model[i].' + col['columnnamecap'] + ';')
		self.writeline(f, 4, '\n')
		
		self.writeline(f, 4, 'e += db.InsertExec(sql, parameters);')
		self.writeline(f, 4, 'if(e != "" && e != null)')
		self.writeline(f, 4, '{')
		self.writeline(f, 5, 'e += \"Error in insert!\"')
		self.writeline(f, 5, 'return false')
		self.writeline(f, 4, '}')
		self.writeline(f, 3, 'return true')
		self.writeline(f, 3, '}')
		self.writeline(f, 2, '}')