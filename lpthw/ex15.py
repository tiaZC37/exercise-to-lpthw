from sys import argv #导入模块sys，使用argv

script, filename = argv #加入两个参数

# filename = input("> ")

txt = open(filename) #打开文件，放入txt变量

print(f"Here's your file {filename}:") #输出，空格引用文件名参数（打卡脚本时需要自己输入）
print(txt.read()) #txt，执行read命令，打印出来

print("Type the filename again:") #再输一次文件名
file_again = input("> ") #提示输入，放入变量中

txt_again = open(file_again) #打开文件名文件，放入变量中

print(txt_again.read()) #txt_again，执行read命令，打印出来