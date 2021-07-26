# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
    newmsg = []
    str1 = ""
    for i in msg:
        if i == " ":
            newmsg.append(i)
        if i != " ":
            if i.isupper():
                
                x = ord(i) + shift
                if x < 65:
                    x += 26
                elif x > 90:
                    x -= 26
                    
                    
            if i.islower():
               x = ord(i) + shift
                
               if x < 97:
                    x += 26
               elif x > 122:
                    x -= 26
            
            
            # print(x)
            a = chr(x)
            # print(a)
            # print(i)
            newmsg.append(a)
          #  print(ord(i))
          #  msg = msg.replace(i, a)
       
          
      
    
    return str1.join(newmsg)
    





