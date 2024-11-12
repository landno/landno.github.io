import os
import sys
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
inp = sys.argv[1]
print(bodyH)
jl = []
for j in os.listdir('json'):
      jl.append(json.load(open('json/'+j)))
if inp == 'w':
  for i in natsorted(os.listdir('workbook')):
    if i[-4:] == 'html':
      tit = ''
      for js in jl:
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
      for js in jl:
  
        #print(js)
        #print(js['titleInfo']['title'])
        if js['sectionId'] == 102 and i == 't6.5.html':
          tit = js['titleInfo']['title']
          js['volumeId'] = 'skip'
        if js['sectionId'] == 103 and i == 't6.5a.html':
          tit = js['titleInfo']['title']
          js['volumeId'] = 'skip'
        if js['sectionId'] == 104 and i == 't6.5b.html':
          tit = js['titleInfo']['title']
          js['volumeId'] = 'skip'
        if js['sectionId'] == 105 and i == 't6.5c.html':
          tit = js['titleInfo']['title']
          js['volumeId'] = 'skip'
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

