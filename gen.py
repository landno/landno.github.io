import os
import json
import sys

input_title = sys.argv[1]
if input_title == 't6.5':
	os.system('python3 1.py 102 > text/t6.5.html')
	input_title = 'skip'
if input_title == 't6.5a':
	os.system('python3 1.py 103 > text/t6.5a.html')
	input_title = 'skip'
if input_title == 't6.5b':
	os.system('python3 1.py 104 > text/t6.5b.html')
	input_title = 'skip'
if input_title == 't6.5c':
	os.system('python3 1.py 105 > text/t6.5c.html')
	input_title = 'skip'

if input_title[0] == 't':
	for i in os.listdir('json'):
		js = json.load(open('json/'+i))
		if js['volumeId'] == 'text':
			s = '0'
			c = js['humanId'].split('-')[1]
			if len(js['humanId'].split('-'))>3:
				s = js['humanId'].split('-')[3]
			if input_title.split('.')[0][1:] == c and input_title.split('.')[1] == s:
				os.system('python3 1.py '+str(js['sectionId'])+' > text/'+input_title+'.html')
if input_title[0] == 'w':
	for i in os.listdir('json'):
		js = json.load(open('json/'+i))
		if js['volumeId'] == 'workbook':
			if js['humanId'].split('-')[1] == input_title[1:]:
				os.system('python3 1.py '+str(js['sectionId'])+' > workbook/'+input_title+'.html')

os.system('python3 i.py w > workbook.html')
os.system('python3 i.py t > text.html')
os.system('python3 checkw.py')
os.system('python3 checkt.py')