# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total=0
count=0
for line in fh:
    #if line.startswith("X-DSPAM-Confidence:"):
    #    count=count+1
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        num=line.find(':')
        end= line.find('\n')
        all=line[num+1:end+1]
        final=float(all.lstrip())
        total=total+final
        count=count+1

print("Average spam confidence:", total/count)
