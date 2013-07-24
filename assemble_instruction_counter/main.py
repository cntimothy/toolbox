import os
import operator

for i in range(1, 21):
    filename = str(i) + '.c'
    os.system('/usr/local/mipsel-robin-elf/bin/gcc -S -o1 ' + filename)

dic = {}

ins_list = ['add', 'addu', 'sub', 'subu', 'and', 'or', 'xor', 'nor', 'slt', 'sltu', 'sll', 'srl', 'sra', 'sllv', 'srlv', 'srav', 'jr', 'addi', 'addiu', 'andi', 'ori', 'xori', 'lw', 'sw', 'beq', 'bne', 'slti', 'sltiu', 'lui', 'j', 'jal'] 

detail = open('detail.txt', 'w')

for i in range(1, 21):
	count = 0
	filename = str(i) + '.s'
	detail.write('=========================================='+filename+'==========================================\n')
	f = open(filename)
	LineNo = 1
	for line in f:
		line = line.strip()
		if(not line == 'main:') and (not line.startswith('.')) and (not line.startswith('$') and (line != "")):		
			detail.write('[' + str(LineNo) + ']')
			array = line.split('	')
			array = array[0].split(' ')
			operation = array[0]			
			detail.write("\t" + operation + "\t")
			if dic.has_key(operation):
				dic[operation] += 1
			else:
				dic[operation] = 1
			count += 1
			if count == 10:
				detail.write('\n')
				count = 1
		LineNo += 1
	f.close()
	detail.write('\n')
	
f = open('result.txt', 'w')
sorted_list = sorted(dic.iteritems(), key=operator.itemgetter(1), reverse=True)  
for item in sorted_list:
	f.write(str(item) + '\n')
	
f.write('\n\n********************************************\n\n')	
f.write('Not support instruction:\n\t')
count = 1
for key in dic.keys():
	if not key in ins_list:
		f.write(key + ', ')
		if count == 10:
			f.write('\n')
			count = 1
		count += 1
f.close()

