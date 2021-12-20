from sys import argv

script, user_name, password = argv
prompt = "请输入"

print(f"Hi {user_name}, I'm the {script} script.")
print(f"Please check your password {password}.")
check = input(prompt)

print("I’d like to ask you a few question.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Nor sure where that is.
And you have a {computer}. Nice.
""")#多行格式符号，可以输出多行内容。中间用{}表示空格，来引用括号中的变量