# jo function chya aat variable declare rahto to local variable
# jo function chya baher variable declare rahto an to function madhe pn use hou shkto jr to tyat declare nsnar tr

x = 4 # --> global variable
print(x)
def hello():
    x = 5 # --> local variable
    print(x)
    print("Hello Om")

print(f"the global x is {x}")
hello()
print(f"the global x is {x}")