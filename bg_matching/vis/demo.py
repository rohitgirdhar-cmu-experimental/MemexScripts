import sys
sys.path.append('/home/rgirdhar/data/Software/coding-utils/PyHTMLWriter/src');
from Element import Element
from TableRow import TableRow
from Table import Table
from TableWriter import TableWriter
import os

def readRetrievals(fpath, ):
  f = open(fpath, 'r')
  lines = f.read().splitlines()
  f.close()
  imids = []
  allmatches = []
  for line in lines:
    imgid = int(line.split(';')[0])/10000
    imids.append(imgid)
    matches = line.split(';')[1].strip()
    matches = [(int(m.split(':')[0])/DIV, float(m.split(':')[1])) for m in matches.split()]
    allmatches.append(matches)
  return (imids, allmatches)

t = Table()
methods = ['full.txt']
imgsdir = 'http://10.1.94.128:8000/~rgirdhar/memex/dataset/0001_Backpage/Images/'
imgslistpath = '/memexdata/Dataset/processed/0001_Backpage/Images/lists/Images.txt'
respath = '/memexdata/Dataset/processed/0001_Backpage/Search/results/temp/res'
segdir = 'http://10.1.94.128:8000/~rgirdhar/memex/dataset/0001_Backpage/Features/Segments'
respath_f = '/memexdata/Dataset/processed/0001_Backpage/Search/results/temp/res_fullImg'

f = open(imgslistpath)
imgslist = f.read().splitlines()
f.close()
print len(imgslist)

def readScores(fpath):
  f = open(fpath)
  s = f.read().splitlines()[0]
  if len(s) == 0:
    return([], [])
  f.close()
  matches = s.strip().split()
  imnames = []
  scores = []
  for m in matches[:50]:
    temp = m.strip().split(':')
    imname = imgslist[int(temp[0]) / 10000]
    score = float(temp[1])
    imnames.append(imname)
    scores.append(score)
  return (imnames, scores)

def readScores2(fpath):
  f = open(fpath)
  s = f.read().splitlines()[0]
  if len(s) == 0:
    return([], [])
  f.close()
  matches = s.strip().split()
  imnames = []
  scores = []
  for m in matches[:50]:
    temp = m.strip().split(':')
    imname = imgslist[int(temp[0]) / 10000 - 1]
    score = float(temp[1])
    imnames.append(imname)
    scores.append(score)
  return (imnames, scores)


t = Table()
r= TableRow(isHeader=True)
r.addElement(Element('Sno'))
r.addElement(Element('Method'))
r.addElement(Element('Query/Top Match'))
r.addElement(Element('Matches...'))
for i in range(500):
  fpath = os.path.join(respath, str(i + 1) + '.txt');
  fpath2 = os.path.join(respath_f, str(i + 2) + '.txt');
  imnames, scores = readScores(fpath)
  imnames2, scores2 = readScores2(fpath2)
  if len(imnames) == 0 or len(imnames2) == 0:
    continue
  r = TableRow(rno=i)
  r.addElement(Element('Background'))
  for j in range(20):
    e = Element()
    e.addImg(os.path.join(imgsdir, imnames[j]), 
        overlay_path=os.path.join(segdir, imnames[j]))
    e.addTxt(scores[j])
    r.addElement(e)
  t.addRow(r)
  r = TableRow(rno=i)
  r.addElement(Element('Full Image'))
  for j in range(20):
    e = Element()
    e.addImg(os.path.join(imgsdir, imnames2[j]))
    e.addTxt(scores2[j])
    r.addElement(e)
  t.addRow(r)


tw = TableWriter(t, 'out')
tw.write()


