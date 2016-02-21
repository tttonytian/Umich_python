name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
names = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    names.append(words[1])
    
for name in names:
    counts[name] = counts.get(name, 0) + 1
    
bigcount = None
bigname = None
for name,count in counts.items():
    if bigcount is None or count > bigcount:
        bigname = name
        bigcount = count

print bigname,bigcount
