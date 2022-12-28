#Goal: Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#Output the email and the count as such: "Email count"

#adapted Code from Chp 8 assignment to create a list of all the emails in the .txt file
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

emails = list()
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    emails.append(words[1])
#print(emails)

#Code to create a dictionary of emails with counts
counts = dict()
for email in emails:
    counts[email] = counts.get(email, 0) + 1

#determines largest email in dictionary
most_e = None
most_count = None
for email, count in counts.items():
    if most_count is None or count > most_count:
        most_count = count
        most_e = email
print(most_e, most_count)
