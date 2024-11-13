import os
from bs4 import BeautifulSoup
count=0
for i in os.listdir('xhtml'):
	print('count:'+str(722-count))
	count+=1
	soup = BeautifulSoup(open('xhtml/'+i).read(),'html.parser')
	#soup = BeautifulSoup(open('xhtml/3.xhtml').read(),'html.parser')
	h = soup.find('h1')
	if h:
		if h.text == '1 正文導言':
			os.system('cp xhtml/'+i+' x_html/text-intro.html')
			break
		