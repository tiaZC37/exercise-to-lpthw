from sys import argv

script, filename = argv

txt = open(filename)

print(txt.read()) #对变量txt储存的东西进行read命令