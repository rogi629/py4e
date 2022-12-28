#Goal: Take a file, find X-DSPAM-Confidence, and print average of all floating point values
# Use the file name mbox-short.txt || PY4E playground has the file stored in it.
#This program is written with the assumption it will be copy/pasted into PY4E
fname = input("Enter file name: ")
fh = open(fname)
count = 0
value = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count += 1
    colpos = line.find(":")
    value = float(line[colpos+1:]) + value
avg = value/count
print("Average spam confidence:", avg)
