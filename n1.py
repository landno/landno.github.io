import os
import json
from natsort import natsorted
bodyH='''
<html>
  <head>
    <style>
      a {
        color:black;
        font-size:10pt;
        margin:10pt;
      }
    </style>
  </head>
  <body>
'''
bodyF='''
  </body>
</html>
'''
print(bodyH)
for j in natsorted(os.listdir('json')):
	js = json.load(open('json/'+j))
	tit = ''
	if js['titleInfo'].get('title'):
		tit = js['titleInfo']['title']
	else:
		tit = js['seoTitle'].split('|')[0]
	if len(tit)>50:
		tit = tit[0:50]+'...'
	#print(js['humanId']+':'+tit)
	print('  <a href="%s">%s</a><br>'%('html/'+js['humanId']+'.html',js['humanId']+':'+tit))
print(bodyF)