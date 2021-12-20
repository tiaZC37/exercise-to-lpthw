def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

#可以直接输入所需变量
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

#首先先定义变量，再在函数中引用变量放在对应位置作为输入
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#通过直接在函数对应的变量位置进行数学计算，得到相应变量
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)
#通过申明的变量，并进行数学方式生成函数所需的变量
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)