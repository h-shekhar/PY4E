import re
temp = list()
fhan = open('regex_sum_938376.txt')
inp = fhan.read()
inpNum = re.findall('[0-9]+', inp)
for i in inpNum:
    y = int(i)
    temp.append(y)
print(sum(temp))
