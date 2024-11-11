import os
import json
import sys

input_title = sys.argv[1]


if input_title[0] == 't':
	pass
if input_title[0] == 'w':
	for i in os.listdir('json'):
		js = json.load(open('json/'+i))
		if js['volumeId'] == 'workbook':
			if js['humanId'].split('-')[1] == input_title[1:]:
				os.system('python3 1.py '+str(js['sectionId'])+' > workbook/'+input_title+'.html')

os.system('python3 i.py w > workbook.html')