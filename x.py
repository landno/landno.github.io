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
		if t == '4 導言':
			os.system('cp xhtml/'+i+' x_html/chap-4-intro.html')
		if t == '5 導言':
			os.system('cp xhtml/'+i+' x_html/chap-5-intro.html')
		if t == '6 導言':
			os.system('cp xhtml/'+i+' x_html/chap-6-intro.html')
		if t == '10 導言':
			os.system('cp xhtml/'+i+' x_html/chap-10-intro.html')
		if t == '11 導言':
			os.system('cp xhtml/'+i+' x_html/chap-11-intro.html')
		if t == '13 導言':
			os.system('cp xhtml/'+i+' x_html/chap-13-intro.html')
		if t == '14 導言':
			os.system('cp xhtml/'+i+' x_html/chap-14-intro.html')
		if t == '21 導言':
			os.system('cp xhtml/'+i+' x_html/chap-21-intro.html')
		if t == '22 導言':
			os.system('cp xhtml/'+i+' x_html/chap-22-intro.html')
		if t == '23 導言':
			os.system('cp xhtml/'+i+' x_html/chap-23-intro.html')
		if t == '24 導言':
			os.system('cp xhtml/'+i+' x_html/chap-24-intro.html')
		if t == '25 導言':
			os.system('cp xhtml/'+i+' x_html/chap-25-intro.html')
		if t == '30 導言':
			os.system('cp xhtml/'+i+' x_html/chap-30-intro.html')
			#break
		if len(t.split(' ')) == 2 and meta['content'][34:36] == '1.':
			if len(t.split(' ')[0].split('-')) == 2:
				fn = 'chap-'+t.split(' ')[0].split('-')[0]+'-sect-'+t.split(' ')[0].split('-')[1]+'.html'
				os.system('cp xhtml/'+i+' x_html/'+fn)