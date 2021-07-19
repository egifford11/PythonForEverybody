name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emcounts = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "):
        continue
    words=line.split()
    emcounts[words[1]] = emcounts.get(words[1],0)+1

bigcount=None
bigword=None
for word in emcounts:
    if bigcount is None:
        bigcount= emcounts[word]
    if bigcount < emcounts[word]:
        bigcount= emcounts[word]
        bigword=word

print(bigword, bigcount)
