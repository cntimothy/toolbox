#!c:\python27\python.exe
#filename:xmltocs.xml

from table import Table
from xml.etree import ElementTree
from linefac import Linefac
from doc import Doc
import os

class XMLToCs:
	def __init__(self, filepath):
		self.filepath = filepath;
		self.datatables = []
		self.doc = Doc()
		
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
			
	def initialdoc(self):
		self.doc.clear()
		
	def buildmodel(self):
		for model in self.datatables:
			self.initialdoc()
			self.doc.append(Linefac.genlineobj('using System;'))
			self.doc.append(Linefac.genlineobj('using System.Colllesections.Generic;;'))
			self.doc.append(Linefac.genlineobj('using System.Linq;'))
			self.doc.append(Linefac.genlineobj('using System.Web;'))
			self.doc.append(Linefac.genlineobj(''))
			self.doc.append(Linefac.genlineobj('namespace Model'))
			self.doc.append(Linefac.genlineobj('{'))
			self.doc.append(Linefac.genlineobj('public class' + model.tablenamecap))
			self.doc.append(Linefac.genlineobj('{'))
		
			for field in model.columns:
				self.doc.append(Linefac.genlineobj('private ' + field['columnnettype'] + ' ' + field['columnname'] + ';'))
		
			self.doc.append(Linefac.genlineobj(''))
			for field in model.columns:
				self.doc.append(Linefac.genlineobj('public ' + field['columnnettype'] + ' ' + field['columnnamecap']))
				self.doc.append(Linefac.genlineobj('{'))
				self.doc.append(Linefac.genlineobj('get { return ' + field['columnname'] + '; }'))
				self.doc.append(Linefac.genlineobj('set { ' + field['columnname'] + ' = value; }'))
				self.doc.append(Linefac.genlineobj('}'))
			self.doc.append(Linefac.genlineobj('}'))
			self.doc.append(Linefac.genlineobj('}'))
		
			self.writemodel(model)
		
	def writemodel(self, model):
		if (not os.path.exists('Model')) or (os.path.isfile('Model')):
			os.makedirs('Model')
		f = file("Model\\" + model.tablenamecap + '.cs', 'w')
		self.doc.writeall(f)
		print 'Model:', model.tablenamecap, 'is Done!'
		
	def buildbll(self):
		for model in self.datatables:
			self.initialdoc()
			self.doc.append(Linefac.genlineobj('using System;'))
			self.doc.append(Linefac.genlineobj('using System.Colllesections.Generic;'))
			self.doc.append(Linefac.genlineobj('using System.Linq;'))
			self.doc.append(Linefac.genlineobj('using System.Web;'))
			self.doc.append(Linefac.genlineobj('using System.Data;'))
			self.doc.append(Linefac.genlineobj('using System.Data.SqlClient;'))
			self.doc.append(Linefac.genlineobj('using DBUnity;'))
			self.doc.append(Linefac.genlineobj('using Model;'))
			self.doc.append(Linefac.genlineobj('using System.Text;'))
			self.doc.append(Linefac.genlineobj(''))
			self.doc.append(Linefac.genlineobj('namespace BLL'))
			self.doc.append(Linefac.genlineobj('{'))
			self.doc.append(Linefac.genlineobj('public class' + model.tablenamecap + "BLL()"))
			self.doc.append(Linefac.genlineobj('{'))
			self.doc.append(Linefac.genlineobj('public ' + model.tablenamecap + 'BLL(){}'))
			self.doc.append(Linefac.genlineobj(''))
			self.doc.append(Linefac.genlineobj('static readonly SQLDatabase db = new SQLDatabase();'))
			self.doc.append(Linefac.genlineobj(''))
			self.buildinsert(model)
			self.buildselect(model)
			self.buildupdate(model)
			self.builddelete(model)
			self.doc.append(Linefac.genlineobj('}'))
			self.doc.append(Linefac.genlineobj('}'))
			
			self.writebll(model)
		
	def writebll(self, model):
		if (not os.path.exists('BLL')) or (os.path.isfile('BLL')):
			os.makedirs('BLL')
		f = file("BLL\\" + model.tablenamecap + 'BLL.cs', 'w')
		self.doc.writeall(f)
		print 'BLL:', model.tablenamecap, 'BLL is Done!'
	
	def buildinsert(self, model):
		self.doc.append(Linefac.genlineobj('public static bool Insert(List<' + model.tablenamecap + '> models, ref string e)'))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj('int count = models.Count;'))
		self.doc.append(Linefac.genlineobj('for(int i = 0; i < count; i++)'))
		self.doc.append(Linefac.genlineobj('{'))
		
		strsql = 'insert into sb_' + model.tablenamecap + '('
		strsql += ','.join(model.columnnamelist) + ')'
		strsql += 'values(@'
		strsql += ",@".join(model.columnnamelist) + ')'		
		self.doc.append(Linefac.genlineobj('string sql = \"' + strsql + '\";'))
		
		self.doc.append(Linefac.genlineobj('SqlParameter[] pamaters = '))
		self.doc.append(Linefac.genlineobj('{'))
		
		templist = []
		for col in model.columns:			
			templist.append('new SqlParameter(\"@' + col['columnname'] + '\", SqlDbType.' + col['columnsqldbtype'] + ', ' + col['columnsqldbwidth'] + ')')
		tempstr = ', '.join(templist)
		self.doc.append(Linefac.genlineobj(tempstr))
		self.doc.append(Linefac.genlineobj('};'))
		
		tempcount = 0
		for col in model.columns:
			self.doc.append(Linefac.genlineobj('parameters[' + str(tempcount) + '].Value = model[i].' + col['columnnamecap'] + ';'))
			tempcount = tempcount + 1
		self.doc.append(Linefac.genlineobj(''))
		
		self.doc.append(Linefac.genlineobj('e += db.InsertExec(sql, parameters);'))
		self.doc.append(Linefac.genlineobj('if(e != "")'))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj('e += \"Error in insert!\"'))
		self.doc.append(Linefac.genlineobj('return false'))
		self.doc.append(Linefac.genlineobj('}'))
		self.doc.append(Linefac.genlineobj('return true'))
		self.doc.append(Linefac.genlineobj('}'))
		self.doc.append(Linefac.genlineobj('}'))
		
	def buildselect(self, model):
		self.doc.append(Linefac.genlineobj('public static bool Select(List<' + model.tablenamecap +'> models, string sql, ref string e)'))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj('DataTable table = new DataTable();'))
		self.doc.append(Linefac.genlineobj('table = db.QueryDataTable(sql, ref e);'))
		self.doc.append(Linefac.genlineobj('if (e != "")'))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj('for (int i = 0; i < table.Rows.Count; i++)'))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj(model.tablenamecap + 'model = new ' + model.tablenamecap + '();'))
		
		for col in model.columns:
			self.doc.append(Linefac.genlineobj('model.' + col['columnnamecap'] + ' = (' + col['columnnettype'] + ')table.Rows[i][\"' + col['columnname'] + '\"];'))
		self.doc.append(Linefac.genlineobj('models.Add(model);'))
		
		self.doc.append(Linefac.genlineobj('}'))
		self.doc.append(Linefac.genlineobj('return true;'))
		self.doc.append(Linefac.genlineobj('}'))
		self.doc.append(Linefac.genlineobj('else'))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj('e += \"Error in select!\"'))
		self.doc.append(Linefac.genlineobj('return false;'))
		self.doc.append(Linefac.genlineobj('}'))
		self.doc.append(Linefac.genlineobj('}'))
		
	def buildupdate(self, model):
		self.doc.append(Linefac.genlineobj('public static bool Update(' + model.tablenamecap + ' model, ref string e'))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj('StringBuilder strSql = new StringBuilder();'))
		self.doc.append(Linefac.genlineobj('strSql.Append(\"update tb_' + model.tablenamecap + ' set \");'))
		for col in model.columns[1:]:
			self.doc.append(Linefac.genlineobj('strSql.Append(\"' + col['columnname'] + '=@' + col['columnname'] + ',\");'))
		self.doc.append(Linefac.genlineobj('strSql.Append(\" where ' + model.columns[0]['columnname'] + '=@' + model.columns[0]['columnname'] + ' \");'))
		
		self.doc.append(Linefac.genlineobj('SqlParameter[] pamaters = '))
		self.doc.append(Linefac.genlineobj('{'))
		
		templist = []
		for col in model.columns:			
			templist.append('new SqlParameter(\"@' + col['columnname'] + '\", SqlDbType.' + col['columnsqldbtype'] + ', ' + col['columnsqldbwidth'] + ')')
		tempstr = ', '.join(templist)
		self.doc.append(Linefac.genlineobj(tempstr))
		self.doc.append(Linefac.genlineobj('};'))
		
		tempcount = 0
		for col in model.columns:
			self.doc.append(Linefac.genlineobj('parameters[' + str(tempcount) + '].Value = model[i].' + col['columnnamecap'] + ';'))
			tempcount = tempcount + 1
		self.doc.append(Linefac.genlineobj(''))
		
		self.doc.append(Linefac.genlineobj('e = db.QueryExec(strSql.ToString(), parameters);'))
		self.doc.append(Linefac.genlineobj('if(e != "")'))
		self.doc.append(Linefac.genlineobj('{'))		
		self.doc.append(Linefac.genlineobj('e += \"Error in update!\"'))
		self.doc.append(Linefac.genlineobj('return false;'))
		self.doc.append(Linefac.genlineobj('}'))
		self.doc.append(Linefac.genlineobj('return true;'))
		self.doc.append(Linefac.genlineobj('}'))
		
	def builddelete(self, model):		
		self.doc.append(Linefac.genlineobj('public static bool delete(' + model.columns[0]['columnnettype'] + " key, ref string e)"))
		self.doc.append(Linefac.genlineobj('{'))
		self.doc.append(Linefac.genlineobj('StringBuilder strSql = new StringBuilder();'))
		self.doc.append(Linefac.genlineobj('strSql.Append(\"delete from tb_' + model.tablenamecap + ' \");'))
		self.doc.append(Linefac.genlineobj('strSql.Append(\" where ' + model.columns[0]['columnname'] + '=@' + model.columns[0]['columnname'] + ' \");'))
		self.doc.append(Linefac.genlineobj('SqlParameter[] parameters = { new SqlParameter(\"@' + model.columns[0]['columnname'] + '\", SqlDbType.' + model.columns[0]['columnsqldbtype'] + ',' + model.columns[0]['columnsqldbwidth'] + ')};'))
		self.doc.append(Linefac.genlineobj('parameters[0].Value = key;'))
		self.doc.append(Linefac.genlineobj('e = db.QueryExec(strSql.ToString(), parameters);'))
		self.doc.append(Linefac.genlineobj('if(e != "")'))
		self.doc.append(Linefac.genlineobj('{'))		
		self.doc.append(Linefac.genlineobj('e += \"Error in delete!\"'))
		self.doc.append(Linefac.genlineobj('return false;'))
		self.doc.append(Linefac.genlineobj('}'))
		self.doc.append(Linefac.genlineobj('return true;'))
		self.doc.append(Linefac.genlineobj('}'))