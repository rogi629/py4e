#In this assignment you will read through and parse a file with text and numbers.
#You will extract all the numbers in the file and compute the sum of the numbers.
#The basic outline of this problem is to read the file, look for integers using the re.findall(),
#looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers and summing up the integers.

#Code inputs file name, defaulting 2 file names
name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_sample.txt"
elif len(name) == 1:
    name = "regex_sum_actual.txt"
fh = open(name)

import re
time = list()
#Code creates a regular expression find for all nums in the text file
for line in fh:
    line = line.rstrip()
    nums = re.findall('[0-9]+', line)
    #Code skips lines with no nums, and adds each num from each line
    if len(nums) <= 0: continue
    for num in nums:
        time.append(num)
#print(nums)
#print (time)

sum = 0
for num in time:
    sum = sum + int(num)
print (sum)
