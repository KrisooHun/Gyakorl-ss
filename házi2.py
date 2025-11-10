def password(passw):
    count = -1
    if len(passw) >= 8:
        for r in passw:               
            if r.isupper():
                return         
        for i in passw:
            count += 1
            passw[count] = ["123456789"]
            return
            
         




 
passw = input("adjon meg egy jelszót: ")
print(password(passw))