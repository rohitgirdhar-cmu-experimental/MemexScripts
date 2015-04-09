inpath = '/memexdata/Dataset/processed/0002_BackpageComplete/Images/lists/Images.txt'
outpath = '/memexdata/Dataset/processed/0002_BackpageComplete/Images/lists/Images_nospaces.txt'

f = open(inpath)
fnames = f.read().splitlines()
f.close()

f = open(outpath, 'w')
for fname in fnames:
  if ' ' in fname:  
    fname = fname.replace(' ', '')
    fname = '../corpus_nospaces/' + fname
  f.write(fname + '\n')
f.close()

