filename = 'sample.txt'
try:
    file1 = open(filename,'r')
    reading = file1.read()
    print(reading)
    file1.close()

except FileNotFoundError:
    print('The file',filename,'was nor found')