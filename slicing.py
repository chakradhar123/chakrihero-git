
fname = input("Enter file name: ")
fh = open(fname)

t=0
c=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x=line.find('0')
    t=t+float(line[x:])
    c=c+1
    
print("Average spam confidence:",t/c)
