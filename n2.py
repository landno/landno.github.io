import os
import json
import sys
from natsort import natsorted
from bs4 import BeautifulSoup

bodyH='''
<!DOCTYPE html>
<head>
<meta charset=UTF-8>
<link rel="stylesheet" href="../style.css">
<script src="../jquery-3.7.1.min.js"></script>
<script src="../acim.js"></script>
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
	with open('epub/'+i) as f:
		r_lst.append(f.read())

#print(bodyH)
js = json.load(open('json/'+num+'.json'))
tit = ''
if js['titleInfo'].get('title'):
	tit = js['annotation']+':'+js['titleInfo']['title']
else:
	tit = js['seoTitle'].split('|')[0]
print('<div id="title">%s</div>'%tit)
tag = ''
r_t_lst = []
x_t_lst = []
if js['volumeId'] == 'text':
	tag = js['annotation']+'.'
for i in r_lst:
	#print(i)
	soup = BeautifulSoup(i,'html.parser')
	content = soup.text
	for i in range(1,30):
		r = content.find(tag+str(i))
		if r>0:
			r2 = content.find(tag+str(i+1))
			if r2>0:
				r_t_lst.append(content[r:r2])
			else:
				r_t_lst.append(content[r:])

for i in r_t_lst:
	#j = i[len(tag):].find('.')

	#first
	k = i.find('2',len(tag)+3)
	if k>0:
		print(i[0:k].strip()+'here')
	else:
		print(i.strip()+'hrer')

	#last
	for k in range(2,30):
		c1 = i.find(str(k),len(tag)+3)
		c2 = i.find(str(k+1))
		if c1>0 and c2>0:
			print(i[c1:c2].strip())
		elif c1>0 and c2<0:
			print(i[c1:].strip())
#print(r_t_lst)
x_soup = BeautifulSoup(open('x_html/'+js['humanId']+'.html'),'html.parser')


for i in x_soup.find_all('p'):
	#print(i)
	k = ['0','1','2','3','4','5','6','7','8','9']
	if str(i)[3:4] in k:
		x_t_lst.append(i.text)
	else:
		x_t_lst[len(x_t_lst)-1]=str(x_t_lst[len(x_t_lst)-1])+i.text
		#print(str(i)[3:4]+' not num')
	#print(i.text.strip())

for i in x_t_lst:
	for j in range(2,30):
		print(j)
#print(js['bodyHtml'])
#print(bodyF)