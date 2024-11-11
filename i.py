import os
import sys
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
      t = i.split('.')[0]
      print('  <a href="%s">%s</a>'%('workbook/'+i,t))
if inp == 't':
  for i in natsorted(os.listdir('text')):
    if i[-4:] == 'html':
      t = i.split('.')[0]
      print('  <a href="%s">%s</a>'%('text/'+i,i[0:-5]))
print(bodyF)
