from xmltocs import XMLToCs
while True:
	path = raw_input("Please enter filepath:")
	if path:
		break
print 'The filepath you enter is', path
paser = XMLToCs(path)
paser.transfer()
paser.writebll()
