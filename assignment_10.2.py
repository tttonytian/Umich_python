name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

time = list()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time.append(words[5])
