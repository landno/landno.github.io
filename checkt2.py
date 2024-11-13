import os
from bs4 import BeautifulSoup
import numpy as np
count = 0
for i in os.listdir('html'):
	if i[-4:] == 'html':
		with open('html/'+i) as f:
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
						#print(j)
						k = int(j['tid'].split('#')[1].split(':')[0])
						h = int(j['tid'].split('#')[1].split(':')[1])
						if d_id.get(k):
							d_id[k] = d_id[k]+','+str(h)
						else:
							d_id[k] = str(h)
			#print(u_id)
			#print(d_id)
			#if u_count != d_count:
			#print(i+'@@@@@@@@error@@@@@@@')
			#print(i)
			#print(len(u_id))
			#print(len(d_id))

			for k,v in u_id.items():
				if v != d_id[k]:
					#print(len(u_id))
					#print(len(d_id))
					count+=1
					print(u_id[k]+'=not same='+d_id[k]+' in '+str(k))
					print(i)
					#os.system('rm text/'+i)
					print('--------')
print('text total count:'+str(count))