import string, secrets

chrs = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

choose = input("What do you want to print? : ")
length = input("Choose your password length: ")

password_in_chrs = ''.join(secrets.choice(chrs + symbols + numbers) for i in range(int(length)))


print("********************Python Password generator********************")

if choose == "password":
    print(password_in_chrs)