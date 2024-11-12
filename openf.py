import os
import sys
input_less = sys.argv[1]

app = ''
if len(sys.argv)>2:
	app = sys.argv[2]
if app == 's2' or app == 't2':
	if input_less[0] == 't':
		for i in os.listdir('xzc/text'):
			if i == input_less[1:].split('.')[0]:
				for j in os.listdir('xzc/text/'+i):
					if len(j.split(' ')[0].split('-'))<2:
						continue
					c = j.split(' ')[0].split('-')[1]
					if c == input_less[1:].split('.')[1]:
						if app[0] == 's':
							os.system('open -a "/Applications/Sublime Text.app/" "xzc/text/'+i+'/'+j+'"')
						else:
							os.system('open -a TextEdit.app "xzc/text/'+i+'/'+j+'"')

elif input_less[0] == 't':
	for i in os.listdir('miracle_r'):
		if i.split('.')[0] == input_less[1:].split('.')[0]:
			for j in os.listdir('miracle_r/'+i):
				if j.split('.')[0] == input_less[1:].split('.')[1]:
					if app == 's':
						os.system('open -a "/Applications/Sublime Text.app/" miracle_r/'+i+'/'+j)
					else:
						os.system("open -a TextEdit.app miracle_r/"+i+'/'+j)

if input_less[0] == 'w':
	os.system("open -a TextEdit.app miracle_l/"+input_less[1:]+'.txt')
