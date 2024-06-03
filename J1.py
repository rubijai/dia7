# file-handling
# There are three major steps to referencing a file:
# 1.	Open the file:This lets the operating system know the name and location of the file being referenced
#  and how the file is to be used (such as read or write)
# 2.	Perform operations on the file data (such as read, write, or append):
# Now that the operating system has opened the file, it is ready to be used for the purpose specified in step 1
# 3.	Close the file:After the desired set of operations has been completed,
# the operating system must be informed that access to the file is no longer necessary.

#import readline


fhandle = open('examp.txt', 'w')
fhandle.write('This is a write example. ')
fhandle.write('Text will be sequentially written until a newline control character occurs. \n')
fhandle.write('Then a new line will begin with \n')
fhandle.write('and another new line, etc \n')
fhandle.write('Yo soy Jaime Ramírez Arbeláez\n')
fhandle.close()

f2 = open('examp.txt', 'r')
print(f2.read())           # the 'read' method reads the file. Al ejecutar este
                           # método no se deja espacios entre líneas.
f2.close()

print('MMMMM')
print()


f2 = open('examp.txt', 'r')
for line in f2:  ## iterates over the lines of the file, las imprime y deja espacio entre líneas.
    print(line)  #
f2.close()

f3 = open('source.txt', 'w')
f3.write(' 5 \n ')
f3.write('1.4 \n ')
f3.write('0 \n ')
f3.write('1.6 \n ')
f3.write('-4 \n ')
f3.close

f3 = open("source.txt")
for line in f3:
    print(line)
f3.close()

print('!!!!!!!')
print()
f3 = open("source.txt")
print(f3.read())
f3.close()

print('MMMMM')
print()
f3 = open("source.txt")
print(f'f3.readline() {f3.readline()}')  # print(readline()) imprime una sola línea                         5
print(f'f3.readlines() {f3.readlines()}')  # print(readlines()) imprime todas las líneas en una sola lista    ['1.4 \n','0 \n ','1.6 \n ','-4 \n ' ]
f3.close
print('MMMMM')
print()


mySource = open("source.txt")
print(mySource.read())
# prisnant(text)
mySource.close()

print('MMMMM')
mySource = open("source.txt")
for line in mySource:
    print(line)
mySource.close()

mySource = open("source.txt")
text = mySource.read()
print(text)
mySource.close()

print('VVVVVVVVVVVV')
mySource = open("source.txt ")
s = 0
for line in mySource:
    print(line)
    line = line.rstrip()
    print(line)
    numbers = line.split()
    print(numbers)
    for x in numbers:
        print(float(x))
        s += float(x)
mySource.close()
print("The sum of all values is", s)

f5 = open('source2.txt', 'w')
f5.write(' 1 8 9.2 -5 \n ')
f5.write('0 12 -23 -9 1 \n ')
f5.write('1.6 2.3 -9.1 \n ')
f5.write('-10 -91 76 23 7 \n ')
f5.write('1.4 9 8 \n ')
f5.close

f5 = open("source2.txt ")
# print(f5.read()) #cambia el formato
s = 0
for line in f5:
    print(line)
    line = line.rstrip()
    numbers = line.split()
    # print(numbers)
    for x in numbers:
        s += float(x)
f5.close()
print("The sum of all values is", s)

n = int(input('Entre num ent positivo '))
if n > 0:
    fname = input('Entre el nombre del archivo: ')
    output = open(fname + '.txt', 'w')
    for i in range(1, n + 1):
        output.write(str(i * i) + '\n')
    output.close()
    print('Done! Look for the file', fname + '.txt')
else:
    print('Se espera num ent positivo')
    open(sum.txt)

fx = open('JRAM.txt')
print(fx.readlines())
fx.close

f=open('JRAlectex.txt','w')
f.write('1,8,9.2,-5 \n')
f.write('1.4,9,8,13 \n')
f.write('0,12,-23,-9,1 \n')
f.write('1.6,2.3,-9.1,-5 \n')
f.write('-42,-91,7,23,17 \n')
f.close()

f2=open('JRAlectex.txt')
print(f2.readlines())
f2.close()

f3=open('JRAlectex.txt','a')
f3.write('70.6\n')
f3.close()

f4=open('JRAlectex.txt')
print(f4.readlines())
f4.close()

print('VVVVVVVVVVVVVVV')
f5=open('JRAlectex.txt')
for line in f5:
    print(f5.readlines())
    print('xxxxxxxx')
f5.close()

f6=open('JRAlectex.txt')
s=0
for line in f6:
    line=line.rstrip()
    numbers=line.split(',')
    print(numbers)
    for n in numbers:
        s+=float(n)
f6.close()
print('s = ',s)

fname = 'temp1'
output = open(fname + ".txt",'w')
output.write(str(5)+' ')
output.write(str(7)+' ')
output.close()

output = open(fname + ".txt",'w')
output.write(str(7)+' ')
output.close()

output = open(fname + ".txt",'r')
print(output.readlines())     #temp1 ['5 7 '] reads one line from a file and returns
                              # it as a string con comillas
output.close()


filename = 'test1'
f = open(filename + '.txt','w')
f.write('hello'+' ')
f.write('world'+' ')
f.close()

output = open('test1.txt','r')
print(output.readlines())     #temp1 ['5 7 '] reads one line from a file and
                              # returns it as a string con comillas
output.close()


filename = 'test2'
f = open(filename + '.txt','w')
f.write('hello'+' ')
f.close()

f = open(filename + '.txt','a')
f.write('world'+' ')
f.close()

output = open('test2.txt','r')
print(output.readlines())     #temp1 ['5 7 '] reads one line from a file and returns it as a string con comillas
output.close()

n = 5
fname = 'data'
output = open(fname + ".txt",'w')
output.write(str(n)+' ')
output.close()
print("Done! Look for the file", fname+'.txt')

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


a1=open('data2.txt')
print(a1.read())
a1.close()

f = open('data.txt')
sval = 0
for line in f:
    sval += float(line)
f.close()
print(sval)






list_n = [34, 23, 124, 2345, 4]
#  using list comprehension n_list = [new_item for item in list_n if test]
n_list = [n * n for n in list_n if n < 100]
print(f'n_list = {n_list}')

n1_list = [n for n in list_n if n % 2 == 0]
print(n1_list)

#with open('file1.txt', 'r') as f2:
with open('J.txt', 'r') as f2:
    n2 = f2.readlines()
    print(n2)
n2_l = [int(n) for n in n2]
print(n2_l)

#with open('file2.txt', 'r') as f1:
with open('J.txt', 'r') as f1:
    n1 = f1.readlines()
    print(n1)
n1_l = [int(n) for n in n1 if int(n) in n2_l]
print(n1_l)

# new_dict = {new_key:new_value for item in list}     dictionary comprehension
# new_dict = {new_key:new_value for (key,value) in dict.items() if test}



with open('sum.txt') as j3:
    numbers = j3.readlines()
    print(numbers)
    n_numbers = [float(n) for n in numbers]
    print(n_numbers)
    print(sum(n_numbers))