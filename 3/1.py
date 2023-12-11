'''
Business challenge/requirement
LifeTel Telecom is the latest entrant in the highly competitive Telecom market of
Singapore. It issues SIM to the verified users. Till now verification was manual
through the photocopy of approved id card document. However government has
recently introduced Social ID called Reference ID which is mapped to fingerprint of
user. LifeTel should now verify user against the fingerprint and Reference ID
Key issues
Build a system where when user enters Reference ID it is encrypted, so that hackers
cannot view the mapping of Reference ID and finger print
Considerations
System should be secure
Data volume
- NA
Additional information
- NA
Business benefits
Company will be able to quickly issue SIM to user and expected gain in volume is
approximately 10 times as the manual process of verification is replaced with secure
automated system.
Approach to Solve
You have to use fundamentals of Python taught in module 2
1. Read the input from command line – Reference ID
2. Check for validity – it should be 12 digits and allows on number and alphabet
3. Encrypt the Reference ID and print it for reference
'''

# Import the PyCrypto library
# import Crypto

def Valocial(str1):
    leng=0
    alpa=0
    num=0

    if len(str1)==12:
        leng=1
            # print("Please enter correct social code")
    str2=list(str1)
    for i in str2:
               
        if i.isalpha():
            alpa=1
            
            # "Please enter correct social code"
        
        if i.isdigit():
             num=1
            # "Please enter correct social code"

    # if (alpa+num+leng)<3:
    #     print( "Invalid Social Security Number Entered")
    #     return 0
    # else:
    #     print( "Valid Social Security Number Entered")
    #     return 1
    return (alpa+num+leng)


telstr1=input("Enter Subscriber Name: ")
telstr2=input("Enter Social ID(Reference ID: ")
# telstr2=Valocial(input("Enter Social ID(Reference ID: "))
# Valocial(input("Enter Social ID(Reference ID: "))

# x=Valocial(telstr2)
p=Valocial(telstr2)
# print(x)    

if p==3:
    print( "Valid Social Security Number")
    telstr2Enc=telstr2.rjust(32)
    #     return 0
    
    # Secret key (pw)
    key = b'1234567890123456'
    cipher = Crypto.Cipher.AES.new(key)
    # Encrypt the string
    encrypted_string = cipher.encrypt(telstr2Enc.encode())

    # Decrypt the encrypted string
    decrypted_string = cipher.decrypt(encrypted_string)

    # Print the original and decrypted strings
    print("Original String:", telstr2Enc)
    print("Decrypted String:", decrypted_string.decode())

else:
    print( "InValid Social Security Number Entered")
