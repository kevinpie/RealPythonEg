my_output_file = open("hello.txt",'a')
my_output_file.writelines("\nThis is my first file")
next_line = ["\nNon Sequitor"]
my_output_file.writelines(next_line)
my_output_file.close()


my_input_file = open("hello.txt",'r')
for line in my_input_file.readlines():
    print line

my_input_file.close()