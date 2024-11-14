import os
import json
from natsort import natsorted
for i in natsorted(os.listdir('json')):
	for j in range(0,85):
		if i.split('.')[0] == str(j):
			js = json.load(open('json/'+i))
			print(j)
			os.system('python3 n2.py '+str(j)+' > html/'+js['humanId']+'.html')
os.system('python3 checkt2.py')