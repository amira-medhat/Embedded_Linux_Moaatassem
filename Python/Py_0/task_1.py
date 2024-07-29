ls = list(map(int, input().split()))
print(ls)
x = ls.count(4)
print(x)

print("-------------------------------------------------------")
############

vowel = ['a', 'u', 'o', 'i', 'e']
letter = input()
for i in vowel:
    if i == letter:
        print("vowel")
        exit()

print("not vowel")

print("-------------------------------------------------------")
############

import os

# to print all environment variables
for key, value in os.environ.items():
  print(f"{key}: {value}")

print("-------------------------------------------------------")

# to print PATH in readable appearance
[print(path) for path in os.getenv("PATH").split(";")]


