import sqlite3

#this line of code creates an sqlite file
conn = sqlite3.connect('orgdb.sqlite')
#similar to a file handle
cur = conn.cursor()

#These lines of code eecutes a line of written code in SQL
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
#File reading (see chapter 10)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    #splitting down to email org specifically
    emailparts = email.split('@')
    org = emailparts[1]
    #these lines of code create a count for each org in SQL, if no org, adds a row with val 1
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    #this is how you commit to run. Not usually run every loop
    conn.commit()

# https://www.sqlite.org/lang_select.html
#displays your selection of top 10 count orgs in terminal
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
