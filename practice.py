j1 = open('test1.txt','w')
j1.write('Hola, soy Tim Sawyer\n''Hola Tim yo soy Ruben\n')
j1.write('Hola, soy Tim Sawyer\n')
j1.close()

j2 = open('test1.txt')
for l in j2:
    print(l)
j2.close()

with open('test1.txt') as j3:
    #print(j3.read())
    print(f'j3.readlines() {j3.readlines()}')

with open('sum.txt') as j3:
    s=0
    for line in j3:
        numbers = line.split(',')
        print(numbers)
        for n in numbers:
            x = float(n)
            s += x
            print(s)
        #print(line,type(line))
        #x = int(line)
        #s += x
        print(s)


with open('sum.txt') as j3:
    numbers = j3.readlines()
    print(numbers)
    n_numbers = [float(n) for n in numbers]
    print(n_numbers)
    print(sum(n_numbers))

fname = 'temp1'
output = open(fname + ".txt", 'w')
output.write(str(5) + ' ')
output.write(str(7) + ' ')
output.close()



fname = 'temp2'
output = open(fname + ".txt", 'w')
output.write(str(5) + ' ')
output.close()

output = open(fname + ".txt", 'w')
output.write(str(7) + ' ')
output.close()


filename = 'test1'
f = open(filename + '.txt','w')
f.write('hello'+' ')
f.write('world'+' ')
f.close()


filename = 'test2'
f = open(filename + '.txt','w')
f.write('hello'+' ')
f.close()

f = open(filename + '.txt','a')
f.write('world'+' ')
f.close()





n = 5
fname = 'data1'
output1 = open(fname + ".txt",'w')
for i in range(1,n+1):
    output1.write(str(3*i+1)+' ')
output1.close()



n = 5
fname = 'data2'
output2 = open(fname + ".txt",'w')
for i in range(1,n+1):
    output2.write(str(3*i+1)+' '+'\n')
output2.close()

f = open('data2.txt')
sval = 0
for line in f:
    print(line)
    sval += float(line)
f.close()
print(sval)


f = open('JRA.txt')
s = 0
for line in f:
    line = line.rstrip()
    numbers = line.split(' ')
    for item in numbers:
        s += float(item)
f.close()
print(s)


f = open('JRA.txt')
numbers=f.readline()
numbers=numbers.rstrip('\n')
print(numbers)
numbers=f.readline()
numbers=numbers.rstrip('\n')
print(numbers)
f.close()