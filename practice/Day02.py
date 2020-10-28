#primitive data type
"""Integer
String
Float
Boolean
"""

#Type Casting
"""
"""

x = 1
print(x)
print(float(x))
print(str(x))

print(bool(0))
print(bool(1))
print(bool(2))
print(bool(-1))

# List
l = [1, 2, 3]
l.insert(0,10)
print(l)
ll = ["mon", "tue", "wed"]
lll = ["russel", 32, True]
print(lll)
lll.append('salary')

print(lll)

print(lll[1])

#list is iterable
for item in lll:
    print(item)


#indexing slicing striding
digits = [1,2,3,4,5,6,7,8,9,0]
print(digits[0]) # 1
print(digits[-1]) # 0
print(digits[-2]) # 9

print(digits[:3])#begin to 3-1
print(digits[5:])#from 5 to end
print(digits[1:6])#print 2,3,4,5,6, index 1 to 5, starting index is inclusive, ending index is exclusive
print(digits[1:10:2])#increment by 2
print(digits[::-2])#backward and increment by 2


for i in range(len(digits)+1):
    print(digits[0:i])

range_size = 4
for i in range(len(digits)-(range_size-1)):
    print(digits[i:i+range_size])








