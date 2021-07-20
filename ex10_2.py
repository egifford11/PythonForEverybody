name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emcounts = dict()  #create an empty dictionary
emlst=[]           #create an empty list
for line in handle:
    words=line.split()
    if len(words)> 2 and words[0] == 'From':
        hr=words[5].split(':')
        emcounts[hr[0]] = emcounts.get(hr[0],0)+1
    else: continue

for k,v in emcounts.items():  #k=hour, v=count
    emlst.append((k,v))

emlst.sort()
for k,v in emlst:
    print (k,v)
