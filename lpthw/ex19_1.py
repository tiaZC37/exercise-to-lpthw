#用十种方法调用函数
def books(amount_math_book, amount_chinese_book):
    print(f"Here are {amount_math_book} math books.")
    print(f"Here are {amount_chinese_book} math books.")
    print("Total {} books.".format(amount_math_book + amount_chinese_book))
    print("\n")

#直接赋值
books(2,3)

#定义变量
math_book = 4
chinese_book = 6
books(math_book, chinese_book)

#数学运算
books(1+3, 4+1)

#变量和运算结合
books(math_book * 2, chinese_book + 3)

#用户输入
num_math = int(input('math book number.'))
num_chinese = int(input('Chinese book number.'))
books(num_math, num_chinese)

#