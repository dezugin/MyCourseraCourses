import re
f = open("regex_sum_1367087.txt", "r")
x = f.read() 
y = re.findall('[0-9]+', x)
z=0
for i in y:
    z= z+int(i)
print(z)