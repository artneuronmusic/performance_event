import re


def validate_password(password):
    x = True
    while x:
        if (len(password)<6 or len(password)>16):
            break
        elif not re.search("[a-z]",password):
            break
        elif not re.search("[0-9]",password):
            break
        elif not re.search("[A-Z]",password):
            break
        elif not re.search("[$#@]",password):
            break
        elif re.search("\s",password):
            break
        else:           
            # print("Valid Password")
            x=False
            return "valid"
    if x:
        return "invalid"

def validate_name(name):
    regex = r'[A-Za-z0-9]{6,50}'
    if(re.fullmatch(regex, name)):
        return "valid"
 
    else:
        return "invalid"

  

def validate_email(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return "valid"
 
    else:
        print("Invalid Email")
        return "invalid"
