#Goal: Take a file, and print it in all uppercase letters
#Use words.txt as the file name. PY4E playground has the file stored in it.
#This program is written with the assumption it will be copy/pasted into PY4E
fname = input("Enter file name: ")
fh = open(fname)
for cheese in fh:
    cheese = cheese.rstrip()
    cheese = cheese.upper()
    print(cheese)
