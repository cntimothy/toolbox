#This is a toolbox to reduce mechanical work.

##xmlparser
###It can analysis a .xml file that describes a database to build model and BLL files. These files are critical when you are developing a MVC project.

##classbuilder
###It can analysis a .xml file that describes a class to build a complete class of C#.

##gccsciprtformips
###It can search all .c files in current directory and invoke gcc to compile them to assembly code. It scan the generated .s file to count operation of assembly code and find out those mips operations that is not supported yet.
###It need python in your system. python 2.7,* is tested.
###Useage
####Modify string gcc to your gcc-for-mips comipler.
####run "python mainscript.py".
