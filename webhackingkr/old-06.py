import base64

def encoding(a):
    i=0
    while i<20:
        users = a.encode('utf-8')
        str_base64 = base64.b64encode(users)
        base64_str = str_base64.decode('utf-8')
        a = base64_str
        i+=1
    return a

def replace_text(b):
    b.replace("1", "!").replace("2", "@").replace("3", "$").replace("4", "^").replace("5", "&").replace("6", "*").replace("7", "(").replace("8", ")")
    return b

user = encoding('admin')
user = replace_text(user)

pw = encoding('nimda')
pw = replace_text(pw)

print("user:", user)
print()
print("pw:", pw)