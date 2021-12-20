from sys import argv

script, first = argv

print("The script is called:", script)
print("The first variable is called:", first)

moreVar = input("Next var")
print(f"The variable after {first} is {moreVar}")