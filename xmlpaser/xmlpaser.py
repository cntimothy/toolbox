#!/usr/bin/python2.7
#filename:xmlpaser.py

from table import Table
from xml.etree import ElementTree

class XMLPaser:
    def __init__(self,filepath):
        self.filepath = filepath
        self.datatables = []

    def transfer(self):
        doc = ElementTree.parse(self.filepath)
        root = doc.getroot()
        database = root.getchildren()
        for table in database:
            datatable = Table(table.attrib['tablename'])
            columns = table.getchildren()
            for column in columns:
                datatable.add(column.attrib['columnname'], column.attrib['columntype'], column.attrib['columnwidth'])
            self.datatables.append(datatable)
        return self.datatables

    def showall(self):
        for t in self.datatables:
            t.show()

    def writemodel():
        for datatable in self.datatables:
            f = file(datatable.tablename.capitalize() + '.cs', 'w')
            try:
                f.write('using System;')
                f.write('using System.Collections.Generic;')
                f.write('using System.Linq;')
                f.write('using System.Web;')
            finally:
                f.close()
