problems = 'broke, pale, short, nerdy'
print(problems)

l = problems.split(",")

print(l)

joined = ' and '.join(l)
print(joined)


s = "iS be a string"
if s.lower().find("is") == -1:
    print("No 'is' here!")
else:
    print("Found 'is' in the string.")

