import sys
sys.path.append('/home/rgirdhar/data/Software/coding-utils/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter
import os

imgsdir = 'http://10.1.94.128:8000/~rgirdhar/memex/dataset/0001_Backpage/Images/'
imgslistpath = '/memexdata/Dataset/processed/0001_Backpage/Images/lists/Images.txt'

def matches_prev(a, b):
  if a[:-6] == b[:-6]:
    return True
  else:
    return False
  
f = open(imgslistpath)
imgslist = f.read().splitlines()
f.close()

t = Table()
r = TableRow()
last_name = ''
for i in range(5000):
  e = Element()
  if not matches_prev(imgslist[i], last_name):
    t.addRow(r)
    r = TableRow()
  e.addImg(os.path.join(imgsdir, imgslist[i]))
  r.addElement(e)
  last_name = imgslist[i]
t.addRow(r)

tw = TableWriter(t, 'out')
tw.write()


