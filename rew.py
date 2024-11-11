import os
for i in os.listdir('workbook'):
	if i[0] == 'w':
		lesson = i.split('.')[0]
		os.system('python3 gen.py '+lesson)
