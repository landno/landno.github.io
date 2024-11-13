import os
from bs4 import BeautifulSoup
count=0
for i in os.listdir('xhtml'):
	print('count:'+str(722-count))
	count+=1
	soup = BeautifulSoup(open('xhtml/'+i).read(),'html.parser')
	#soup = BeautifulSoup(open('xhtml/3.xhtml').read(),'html.parser')
	h = soup.find('h1')
	meta = soup.find('meta',attrs={'property':'og:url'})
	#print(meta['content'][34:36])

	if h:
		t = h.text
		if t == '1 正文導言':
			os.system('cp xhtml/'+i+' x_html/text-intro.html')
			#break
		if len(t.split(' ')) == 2 and meta['content'][34:36] == '1.':
			if len(t.split(' ')[0].split('-')) == 2:
				fn = 'chap-'+t.split(' ')[0].split('-')[0]+'-sect-'+t.split(' ')[0].split('-')[1]+'.html'
				os.system('cp xhtml/'+i+' x_html/'+fn)