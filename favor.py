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
print(bodyH)
jl = []
for j in os.listdir('json'):
      jl.append(json.load(open('json/'+j)))
for i in natsorted(os.listdir('favor')):
  if i[-4:] == 'html':
    tit = ''
    for js in jl:
      #print(js)
      if js['humanId'] != i[0:-5]:
        continue
      #print(js['titleInfo']['title'])
      if js['titleInfo'].get('title'):
        tit = js['titleInfo']['title']
      else:
        tit = js['seoTitle'].split('|')[0]
      t = i.split('.')[0]
      print('  <a href="%s">%s</a><br>'%('workbook/'+i,(t+':'+tit)))

print(bodyF)

