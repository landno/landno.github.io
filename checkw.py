import os
from bs4 import BeautifulSoup
import numpy as np
count=0
errp = []
for i in os.listdir('workbook'):
	if i[-4:] == 'html':
		with open('workbook/'+i) as f:
			soup = BeautifulSoup(f.read(),'html.parser')
			res = soup.find_all('div',attrs={'class':'popup'})
			u_count = 0
			d_count = 0
			u_id = {}
			d_id = {}
			for j in res:
				if j.get('tid'):
					if j['tid'][0] == 'u':
						u_count+=1
						k = int(j['tid'].split('#')[1].split(':')[0])
						h = int(j['tid'].split('#')[1].split(':')[1])
						if u_id.get(k):
							u_id[k] = u_id[k]+','+str(h)
						else:
							u_id[k] = str(h)
					if j['tid'][0] == 'd':
						d_count+=1
						k = int(j['tid'].split('#')[1].split(':')[0])
						h = int(j['tid'].split('#')[1].split(':')[1])
						if d_id.get(k):
							d_id[k] = d_id[k]+','+str(h)
						else:
							d_id[k] = str(h)
			
			#print(i+'@@@@@@@@error@@@@@@@')
			#print(len(u_id))
			#print(len(d_id))
			

			if len(d_id) == 0:
				errp.append(i)
				continue
			for j in range(1,len(u_id)+1):
				if u_id[j] != d_id[j]:
					count+=1
					print(u_id[j]+'=not same='+d_id[j]+' in para:'+str(j))
					print('file:'+i)
					#os.system('rm workbook/'+i)
					print('------------')

print('workbook total err:'+str(count))
