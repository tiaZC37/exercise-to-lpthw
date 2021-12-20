from sys import argv

#运行时指定要操作的变量
script, input_file = argv

#定义一个函数，输入变量f，输出f的读取
def print_all(f):
    print(f.read())

#定义函数rewind(译：倒回)，输入变量f，输出对f进行seek(0)命令
def rewind(f):
    f.seek(0)   #定位到文件的第一位0位处，seek把指针放在位置，有第二个变量，0默认绝对位置，1相对位置，2以末尾定位

#定义函数，输入变量line_count行号，f；输出行号和对f进行readline的命令的结果，f相当于定位
def print_a_line(line_count, f):
    print(line_count, f.readline(), end=" ")  #readline读取整行，到\n止，会返回\n也就本身自带空行，可以改成“ ”结束

#打开运行时指定的文件，保存在current中
current_file = open(input_file)

print("First let's print the whole file:\n")

#调用函数print_all，输入打开的文件，输出read文件的结果
print_all(current_file)

print("Now let's rewind, kind of a tape.")

#调用函数rewind，输入打开的文件，输出对文件进行seek(0)操作
rewind(current_file)

print("Let's print three lines:")

#定义变量表示第1行，调用函数，输出行号和文件执行readline操作
current_line = 1
print_a_line(current_line, current_file) #current_line = 1，在line_count位置上输入了

current_line += 1
print_a_line(current_line, current_file) #current_line = 2

current_line += 1
print_a_line(current_line, current_file) #current_line = 3