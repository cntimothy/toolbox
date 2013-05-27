from xmlpaser import XMLPaser

path = raw_input("Please enter filepath:")
paser = XMLPaser(path)
paser.transfer()
paser.showall()
paser.writemodel()
