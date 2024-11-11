import os
for i in os.listdir('text'):
	if i[0] == 't':
		lesson = i.split('.')[0]+'.'+i.split('.')[1]
		print(lesson)
		os.system('python3 gen.py '+lesson)
