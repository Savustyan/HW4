# Read from file
with open('New_File.txt') as file:
    print(file.read())

# Create new file and copy data
with open('New_File.txt') as file_read, open('New_File2.txt', 'a') as file_write:
    file_write.write(file_read.read())

# transformation
with open('New_File.txt', 'r+') as file:
    data = file.read()
    file.write(data.upper())
    file.write('|'.join(data.split(',')))