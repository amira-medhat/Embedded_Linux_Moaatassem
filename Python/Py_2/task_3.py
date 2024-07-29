import sys

ls = sys.argv
print(f"Name of script: {ls[0]}")
if len(ls) > 1:
    print(f"Number of args: {len(ls) - 1}")
    for i, arg in enumerate(ls[1:], start=1):
        print(f"Argument {i}: {arg}")
else:
    print("There's no arguments")
