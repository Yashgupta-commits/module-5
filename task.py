try:
    file1 = open('my_file.txt','r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()

except FileNotFoundError:
    print("error: the file 'my_file.txt was not found")


