filename = 'output.txt'
write_data = input('Enter text to write to file:')

file1 = open(filename,'w')
file1.write(write_data+'\n')
file1.close()
file1.close()
print('Data successfully written to',filename)


append_data = input('Enter additional text to write to append:')

file1 = open(filename,'a')
file1.write(append_data+'\n')
file1.close()
file1.close()
print('Data successfully appended.')

file1 = open(filename,'r')
reading = file1.read()
print(reading)
file1.close()