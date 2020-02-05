## for loop
for i in range(1,11):
  print(i)

## find the occurance of char in string
test_str = "GeeksforGeeks"
freq_char = {} 

for ch in test_str:
  if ch in freq_char:
    freq_char[ch] +=1
  else:
    freq_char[ch] =1


# printing result  
print ("Count of all characters in GeeksforGeeks is : \n" +  str(freq_char)) 
