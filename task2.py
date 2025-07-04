file_text_1 = input("Enter text to write to the file: ")

file1 = open( 'output.txt', 'w' )
file1.write(file_text_1 + "\n")
file1.close()
print("Data successfully written to output.txt\n")

file_text_2 = input("Enter additional text to append: ")

file2 = open("output.txt", "a")
file2.write(file_text_2 + "\n")
file2.close()
print("Data successfully appended.\n")

print("Final content of output.txt:")
file3 = open("output.txt", "r")
print(file3.read())
file3.close()

