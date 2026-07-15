import random
import string
print("****************")
print("Encrypt & Decrypt your messages")
print("****************")
chars=" "+string.punctuation+string.ascii_letters+string.digits;
chars=list("".join(chars))
key=chars.copy();
random.shuffle(key)
#Encrypt message
isrunning=True
while isrunning:    
    message=input("Enter your plain text: ")
    cipper_text="";
    for m in message:
        index=chars.index(m);
        print(index)
        cipper_text+=(key[index]);
    print("*************")
    print("Your encrypted message is:", end=" ")
    print(cipper_text)
    print("*************")
#Decrypt message
    encryptedmessage=input("Enter your encrypted message: ")
    plain_text=""
    for m in encryptedmessage:
        index=key.index(m)
        plain_text+=chars[index]
    print("*************")
    print("Your decrypted message is:", end=" ")
    print(plain_text)
    print("*************")
    exit=input("Want to end the program?(y/n): ").lower()
    if exit=='y':
        isrunning=False
print("The program has been ended")  
