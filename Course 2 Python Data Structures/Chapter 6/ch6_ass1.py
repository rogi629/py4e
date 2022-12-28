#Goal: Find the value after the : in the below string. print the value as a float
print("Chp 6 assignment 1")
text = "X-DSPAM-Confidence:    0.8475"
colpos = text.find(":")
num = text[colpos+1:]
print(float(num))
