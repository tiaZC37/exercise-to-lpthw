tabby_cat = "\tI'm tabbed in." #\t是空格符号，相当于tab
persian_cat = "I'm split\non a line." #\n换行
backslash_cat = "I'm \\ a \\ cat." #表明\是一个符号，要在字符串中显示

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
''' #这一串都得显示 \n换行，回车也可以换行

print(tabby_cat) #打印变量"tabby_cat"
print(persian_cat)
print(backslash_cat)
print(fat_cat)