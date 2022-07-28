import re
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst = re.findall('\\S+@\\S+', s)
data = 'From stephen.mark@uct.zc.za Sat Jan 2008'
# atpos = data.find('@')
# print(atpos)
# sppos = data.find(' ', atpos)
# print(sppos)
# print(data[atpos+1: sppos])
# y = re.findall('@\w+\.\S+', data)
# y = re.findall('@[^ ]*', data)
y = re.findall('^From .*@[^ ]*', data)
print(y)
#[^ ]=>not blank