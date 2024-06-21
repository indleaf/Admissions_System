def validate_password(s):
    u, p, d = 0, 0, 0
    special_char = "!@#$%^&*()_+[]{}|;:,.<>?/"
    if (len(s) >= 10):
        for i in s:
            # counting uppercase alphabets
            if (i.isupper()):
                u+=1           
            # counting digits
            if (i.isdigit()):
                d+=1           
            # counting the mentioned special characters
            if(i in special_char):
                p+=1          
    if (u>=1 and p>=1 and d>1 and d<4):
        y = "Password is valid"
        return y
    else:
        y = "Invalid Password"
        return y
y = validate_password("Humber!221")
print (y)