#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

time = list()
hours = list()
count = 0
#Code creates a list of strings of the 'X'th string in the line beginning with 'From' from the file
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    time.append(words[5])
#print(time)

#Creates a new list of the hours from the previous list split by ':'
for var in time:
    var = var.split(':')
    hours.append(var[0])
#print(hours)

#Code to create a dictionary of hours with counts
counts = dict()
for hour in hours:
    counts[hour] = counts.get(hour, 0) + 1
#print(counts)

#Creates a list of hour, count pairs sorted by hour
#tmp = list()
#for hour, count in counts.items():
#    tmp.append((hour, count))
tmp = sorted([(hour, count) for hour, count in counts.items()])
#print(tmp)
for hour, count in tmp[:]:
    print(hour, count)
