#this one is like your scripts with argv
def print_two(*args):   #定义一个函数，告诉函数我们需要*args，把所有的参数都接受进来
    arg1, arg2 = args   #解包，变量是args这个东西
    print ("arg1: %r, arg2: %r" % (arg1, arg2))    #%r万能符，将%后的参数原样输出，带‘’

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):    #定义函数，函数需要需要两个变量
    print ("arg1: %r, arg2: %r" % (arg1, arg2))    #将输入的变量打印出来

# this just takes one argument
def print_one(arg1):
    print ("arg1: %r" % arg1)

#this one takes no arguments
def print_none():
    print ("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()