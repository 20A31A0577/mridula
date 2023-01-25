password=input("enter your password")
print(password)
email=input("enter email")
print(email)
s="abcdefghijklmnopqrstvuwxyz"
if email[0] in s and email[len(email)-10:]=='@gmail.com':
    print("crt")
else:
    print("not valid")
    
