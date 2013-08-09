import os
import operator

gcc = '/usr/local/mipsel-robin-elf/bin/gcc'

for parent, dirnames, filenames in os.walk(os.getcwd()):
	for filename in filenames:
		if filename.endswith('.c'):
			os.system(gcc + ' -S ' + filename)	
		
ins_list = ['add', 'addu', 'sub', 'subu', 'and', 'or', 'xor', 'nor', 'slt', 'sltu', 'sll', 'srl', 'sra', 'sllv', 'srlv', 'srav', 'jr', 'addi', 'addiu', 'andi', 'ori', 'xori', 'lw', 'sw', 'beq', 'bne', 'slti', 'sltiu', 'lui', 'j', 'jal'] 

dic = {}
dicForSingleFile = {}
try:
	result = open('Result.txt', 'w')
	detail = open('detail.txt', 'w')
	for parent, dirnames, filenames in os.walk(os.getcwd()):
		for filename in filenames:
			if filename.endswith('.s'):
				lineNo = 1
				try:
					f = open(filename)
					detail.write('================================' + filename + '================================\n')
					for line in f:
						line = line.strip()
						if(not line == 'main:') and (not line.startswith('.')) and (not line.startswith('$') and (line != "")):
							array = line.split('	')
							array = array[0].split(' ')
							operation = array[0]
							
							if dic.has_key(operation):
								dic[operation] += 1
							else:
								dic[operation] = 1
								
							if dicForSingleFile.has_key(operation):
								dicForSingleFile[operation] += 1
							else:
								dicForSingleFile[operation] = 1
								
							detail.write('[' + str(lineNo) + ']')
							detail.write(operation + '\t')
						
						lineNo += 1
						
					result.write("******************************" + filename + "******************************\n")
					sorted_list = sorted(dicForSingleFile.iteritems(), key=operator.itemgetter(1), reverse=True)  
					for item in sorted_list:
						result.write(str(item) + '\n')	
					result.write('\nNot support instruction:\n\t')
					count = 1
					for key in dic.keys():
						if not key in ins_list:
							result.write(key + ', ')
							if count == 10:
								result.write('\n')
								count = 1
							count += 1
					dicForSingleFile.clear()
					
					detail.write('\n\n')
					result.write('\n\n')
				finally:
					f.close()
	result.write("\n\nSummary:\n")				
	sorted_list = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)  
	for item in sorted_list:
		result.write(str(item) + '\n')
	result.write('\nNot support instruction:\n\t')
	count = 1
	for key in dic.keys():
		if not key in ins_list:
			result.write(key + ', ')
			if count == 10:
				result.write('\n')
				count = 1
			count += 1
finally:
	result.close()
	
for parent, dirnames, filenames in os.walk(os.getcwd()):
	for filename in filenames:
		if filename.endswith('.c'):
			os.system(gcc + ' -c -g -Wa,-adlhn ' + filename + ' > ' +filename[:-2] + '.merged')	