import os
import subprocess

with open('lists/Images_escaped.txt') as f:
  l = f.read().splitlines()

i = 0
final = []
for line in l:
  dname = os.path.dirname(line)
  fname = os.path.basename(line)
  if line.count(' ') > 0:
    try:
      os.makedirs('corpus_nospaces/' + dname)
    except:
      pass
    cmd = 'cd corpus_nospaces/' + dname + '; ln -s /home/rgirdhar/memexdata/Dataset/processed/0002_BackpageComplete/Images/corpus/' + line + " " + fname.replace(" ", "")
    print cmd
    subprocess.call(cmd, shell=True)

  if i % 100000 == 0:
    print 'Done %d' % i
  i += 1
