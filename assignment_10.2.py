name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

times = list()
segs = list
hrs = list()
counts = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    times.append(words[5])
for time in times:
    segs = time.split(":")
    hrs.append(segs[0])
    
    
for hr in hrs:
    counts[hr] = counts.get(hr, 0) + 1
    
lst = list()
for hr, fq in counts.items():
    lst.append((hr, fq))
    
lst.sort()

for hr, fq in lst:
    print hr, fq
