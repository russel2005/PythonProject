import re

text = "random string. MyName123@website.com. some more randoom text yourName888@company.net,again russel.50_2020-2@company.net"

pattern = re.compile("random string.")

pattern2 = re.compile("[a-zA-Z]")

email_pattern = re.compile("[a-zA-Z0-9]+\@[a-z0-9]+\.[a-z]+")
email_pattern2 = re.compile("[a-zA-Z0-9\.\_\-]+\@[a-z0-9]+\.[a-z]+")
result = pattern.search(text)
result2 = pattern2.search(text)

find_email = email_pattern.findall(text)#findall(text) search all not first one like search(text)
find_email2 = email_pattern2.findall(text)
print(result)
print(result2)
print(find_email)
print(find_email2)