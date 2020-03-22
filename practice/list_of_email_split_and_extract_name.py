email_list = ["russel.islam@gmail.com", "arish.islam@gmail.com", "sadia.momo@gmail.com"]

def get_fullname(email_list):
    fullname = []
    for name in email_list:
        name = name.split('@')[0]
        firstname = name.split('.')[0]
        lastname = name.split('.')[1]
        fullname.append(firstname + ' ' + lastname)
    return fullname


fullname = get_fullname(email_list)
print(fullname)