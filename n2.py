import os
import json
import sys
from natsort import natsorted
from bs4 import BeautifulSoup
scp ='''
<script src="../acim.js"></script>
'''
bodyH='''
<!DOCTYPE html>
<head>
<meta charset=UTF-8>
<link rel="stylesheet" href="../style.css">
<script src="../jquery-3.7.1.min.js"></script>
</head>
<body>

'''
bodyF='''
</body>
</html>
'''
num = sys.argv[1]

r_lst = []
for i in os.listdir('epub'):
	#print(i[-4:])
	if i[-4:] == 'html':
		if os.path.exists('epub/new/'+i):
			with open('epub/new/'+i) as f:
				r_lst.append(f.read())
		else:
			with open('epub/'+i) as f:
				r_lst.append(f.read())

print(bodyH)

js = json.load(open('json/'+num+'.json'))
tit = ''
if js['titleInfo'].get('title'):
	tit = js['annotation']+':'+js['titleInfo']['title']
else:
	tit = js['seoTitle'].split('|')[0]
print('<div id="title">%s</div>'%tit)
print(js['bodyHtml'])
tag = ''
r_t_lst = []
x_t_lst = []
if js['volumeId'] == 'text':
	tag = js['annotation']+'.'
	if js['annotation'] == 'T-2.V-A':
		tag = 'T-2.V.A.'
	if js['annotation'] == 'T-6.V-A':
		tag = 'T-6.V.A.'
	if js['annotation'] == 'T-6.V-B':
		tag = 'T-6.V.B.'
	if js['annotation'] == 'T-6.V-C':
		tag = 'T-6.V.C.'
	for i in r_lst:
		#print(i)
		soup = BeautifulSoup(i,'html.parser')
		content = soup.text
		for i in range(1,80):
			#print(tag+str(i))

			content = content.replace('\n','')
			r = content.find(tag+str(i)+'.')
			if r>0:
				#print(tag+str(i))
				#print(content)
				r2 = content.find(tag+str(i+1)+'.')
				if r2>0:
					r_t_lst.append(content[r:r2])
				else:
					r_t_lst.append(content[r:])
	if int(num)<100:
		num = '0'+num

	#print(r_t_lst)
	for i in r_t_lst:
		#j = i[len(tag):].find('.')

		#first
		k = i.find('2',len(tag)+6)
		if k>0:
			print('<div class="popup" tid="d%s">%s</div>'%(str(num)+'#'+i[len(tag):].split('.')[0]+':1',i[len(tag):k].replace('\n','')))
		else:
			print('<div class="popup" tid="d%s">%s</div>'%(str(num)+'#'+i[len(tag):].split('.')[0]+':1',i[len(tag):].replace('\n','')))

		#last
		for k in range(2,30):
			c1 = i.find(str(k),len(tag)+6)
			c2 = i.find(str(k+1),len(tag)+6)
			if c1>0 and c2>0:
				t = i[c1:c2]
				print('<div class="popup" tid="d%s">%s</div>'%(str(num)+'#'+i[len(tag):].split('.')[0]+':'+t.split(' ')[0],t[len(str(k))+1:].replace('\n','')))
				#print(i[c1:c2].strip())
			elif c1>0 and c2<0:
				t = i[c1:]
				print('<div class="popup" tid="d%s">%s</div>'%(str(num)+'#'+i[len(tag):].split('.')[0]+':'+t.split(' ')[0],t[len(str(k))+1:].replace('\n','')))
				#print(i[c1:].strip())
	#print(r_t_lst)
	f2 = 'x_html/'+js['humanId']+'.html'
	if os.path.exists('x_html/new/'+js['humanId']+'.html'):
		f2 = 'x_html/new/'+js['humanId']+'.html'
	x_soup = BeautifulSoup(open(f2),'html.parser')


	for p in x_soup.find_all('p'):
		#print(p)
		k = ['0','1','2','3','4','5','6','7','8','9']
		if str(p)[3:4] in k:
			x_t_lst.append(p.text)
		else:
			x_t_lst[len(x_t_lst)-1]=str(x_t_lst[len(x_t_lst)-1])+p.text
			#print(str(i)[3:4]+' not num')
		#print(i.text.strip())
	#print(x_t_lst)





	for i in x_t_lst:
		#first
		k = i.find('2',6)
		if k>0:
			#print('<div class="popup" tid="%s">%s</div>'%('u'+input_num+'#'+str(i[0])+':'+str(j+1),i[1][j].strip()+'。'))
			print('<div class="popup" tid="u%s">%s</div>'%(str(num)+'#'+i.split('.')[0]+':1',i[0:k].replace('\n','')))
		else:
			print('<div class="popup" tid="u%s">%s</div>'%(str(num)+'#'+i.split('.')[0]+':1',i[0:].replace('\n','')))
		for j in range(2,30):
			k1 = i.find(str(j),6)
			k2 = i.find(str(j+1),6)
			if k1>0 and k2>0:
				print('<div class="popup" tid="u%s">%s</div>'%(str(num)+'#'+i.split('.')[0]+':'+str(j),i[k1+len(str(j)):k2].replace('\n','')))
			elif k1>0 and k2<0:
				print('<div class="popup" tid="u%s">%s</div>'%(str(num)+'#'+i.split('.')[0]+':'+str(j),i[k1+len(str(j)):].replace('\n','')))

#print(js['bodyHtml'])
print('<div display="none" class="popup" id="utext"></div>')
print('<div display="none" class="popup" id="dtext"></div>')
print(scp)
print(bodyF)