import re

text = "my number is +(090)-386-31650"

#rough pattern 
pattern1  = "\d+.\d+.\d+"

#
pattern2 = ".{2}\d+.+\d+.\d+"

first = re.findall(pattern1,text)
second = re.findall(pattern2,text)
if first != []:
    print("Match gotten with the 1st pattern")
    print(first)
if second != []:
    print("Match gotten with the 2nd pattern")
    print(second)

