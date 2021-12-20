from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")    #打印，将导入到变量filename表达在{}中
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")    #提示进行操作

print("Opening the file...")
target = open(filename, 'w')    #将保存在filename里的文件（比如test.txt）打开，可进行write

print("Truncating the file. Goodbye!")
target.truncate() #附加练习5，w模式下不需要truncate，python中“...并从开头开始编辑，即原有内容会被删除...”

print("Now I'm going to ask you for three lines.")

#进行输入
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# target.write(f"{line1}\n{line2}\n{line3}") 附加练习3，一行写完命令
#target执行write命令，write变量line1、line2、line3
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()