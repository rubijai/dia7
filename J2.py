f = open('JRA.txt', 'w')
f.write('1 2 3 4 \n')
f.write('2 5 6 7 \n')
f.write('3 8 9  \n')
f.write('4 10 \n')
f.write('5 \n')
f.close()

f2 = open('JRA.txt')
print(f2.read())
f2.close()
print('jjjjjjjj')

f3 = open('JRA.txt', 'a')
f3.write('6 \n')
f3.close()

f4 = open('JRA.txt')
print(f4.read())
f4.close()

print('jjjjjjjjjjjj')
f5 = open('JRA.txt')
for line in f5:
    print(f5.readlines())
f5.close()

f6 = open('JRA.txt')
s = 0
for line in f6:
    line = line.rstrip()
    numbers = line.split(' ')
    for n in numbers:
        s += float(n)
f6.close()
print('s = ', s)

f = open('data.txt', 'w')
f.write('1 \n')
f.write('2 \n')
f.write('3 \n')
f.write('4 \n')
f.write('5 \n')
f.close()

f = open('data.txt')
sval = 0
for line in f:
    sval += float(line)
f.close()
print(sval)

f = open('JRA.txt')
numbers = f.readline()
numbers = numbers.rstrip('\n')
print(numbers)
numbers = f.readline()
numbers = numbers.rstrip('\n')
print(numbers)
f.close()

import matplotlib.pyplot as plt

x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
f = open('data.txt', 'w')
for val in x:
    f.write(str(val) + '\n')
f.close()

f = open('data.txt')
w = []
z = []
for val in f:
    t = float(val)
    w.append(t)
    z.append(2 * t)
f.close()
plt.plot(w, z)
plt.savefig('plot.png')

txt = "     banana     "
x = txt
print("of all fruits", x, "is my favorite")
x = txt.rstrip()  # The rstrip() method removes any trailing characters (characters at the end a string),
# space is the default trailing character to remove.
print(x)
print("of all fruits", x, "is my favorite")

txt = "banana,,,,,ssqqqww....."
print(txt)
x = txt.rstrip(",.qsw")
print(x)