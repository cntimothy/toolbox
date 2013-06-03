#!c:\python27\python.exe
#filename:main.py

from xmlreader import XmlReader
from doc import Doc
from linefac import Linefac
import os

doc = Doc()
reader = XmlReader()
classlist = reader.read()
for c in classlist:
	doc.clear()
	doc.append(Linefac.genlineobj('using System;'))
	doc.append(Linefac.genlineobj('using System.Collections.Generic;'))
	doc.append(Linefac.genlineobj('using System.Linq;'))
	doc.append(Linefac.genlineobj('using System.Web;'))
	doc.append(Linefac.genlineobj(''))
	
	namespace = raw_input('Please enter namespace:')
	doc.append(Linefac.genlineobj('namespace ' + namespace))
	doc.append(Linefac.genlineobj('{'))
	doc.append(Linefac.genlineobj('public class ' + c.name))
	doc.append(Linefac.genlineobj('{'))
	doc.merge(c.genclass())
	
	doc.append(Linefac.genlineobj('}'))
	doc.append(Linefac.genlineobj('}'))
	
	if (not os.path.exists('Result')) or (os.path.isfile('Result')):
		os.makedirs('Result')
	f = file('Result\\' + c.name + '.cs', 'w')
	try:
		doc.writeall(f)
		print 'file ' + c.name + '.cs is build!'
	except:
		print 'error occured in build file: ' + c.name + '.cs'
	finally:
		f.close()