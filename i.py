import os
import sys
import json
from natsort import natsorted
bodyH='''
<html>
  <head>
    <style>
      a {
        font-size:30pt;
        margin:30pt;
      }
    </style>
  </head>
  <body>
'''
bodyF='''
  </body>
</html>
'''
inp = sys.argv[1]
print(bodyH)
if inp == 'w':
  for i in natsorted(os.listdir('workbook')):
    if i[-4:] == 'html':
      tit = ''
      for j in os.listdir('json'):
        js = json.load(open('json/'+j))
        
        #print(js)
        #print(js['titleInfo']['title'])
        if js['volumeId'] == 'workbook':
          if js['annotation'].split('-')[1] == i[1:-5]:
            if js['titleInfo'].get('title'):
              tit = js['titleInfo']['title']
            else:
              tit = js['seoTitle'].split('|')[0]
      t = i.split('.')[0]
      print('  <a href="%s">%s</a><br>'%('workbook/'+i,(t+':'+tit)))

if inp == 't':
  for i in natsorted(os.listdir('text')):
    if i[-4:] == 'html':
      tit = ''
      for j in os.listdir('json'):
        js = json.load(open('json/'+j))
        
        #print(js)
        #print(js['titleInfo']['title'])
        if js['volumeId'] == 'text':
          if len(js['humanId'].split('-'))>3:
            if js['humanId'].split('-')[1] == i.split('.')[0][1:] and js['humanId'].split('-')[3] == i.split('.')[1]:
              pass
              if js['titleInfo'].get('title'):
                tit = js['titleInfo']['title']
              else:
                tit = js['seoTitle'].split('|')[0]
      t = i.split('.')[0]
      print('  <a href="%s">%s</a><br>'%('text/'+i,i[0:-5]+':'+tit))
print(bodyF)

