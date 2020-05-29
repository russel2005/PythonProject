# names = ["AJohn", "Mary"]
# found = False # used flag
# for names in names:
#     if names.startswith("J"):
#         print("Found")
#         found = True
#         break
# if not found:
#     print("Not found")

# or, without use flag
names = ["AJohn", "Mary"]
for names in names:
    if names.startswith("J"):
        print("Found")
        break
else:
    print("Not found")