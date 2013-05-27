#!/usr/bin/python2.7
#filename:tablemodule.py

class Table:
    def __init__(self, tablename):
        self.columns = []
	self.tablename = tablename
    
    def add(self, columnname, columntype, columnwidth):
        column = {}
        column['columnname'] = columnname
        column['columntype'] = columntype
        column['columnwidth'] = columnwidth
        self.columns.append(column)

    def show(self):
        print "Table's name:", self.tablename
        for column in self.columns:
            print "\tColumn's name:", column['columnname'],\
                "\tColumn's type:", column['columntype'],\
                "\tColumn's width:", column['columnwidth']
