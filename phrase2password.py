import random
import os
import sys


vowels_as_numbers = {
    'a': '4',
    'e': '3',
    'i': '1',
    'o': '0',
    'A': '4',
    'E': '3',
    'I': '1',
    'O': '0'
}

special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# This function generates the passphrase. Take a passphrase input by the user:
# "Please hire me" strip it, remove spaces, and force it to lowercase: "pleasehireme"
# make every the first and every other characet capitalized: "PlEaSeHiReMe"
# replace vowels (excluding u) with numbers: "Pl34S3H1R3M3"
# add a random letter to the beggining of the password: "dPl34S3H1R3M3" (example)
# then add random special characters to the end of the password until it meets
# the user input password length: "dPl34S3H1R3M3@!" (example)
def password_generate(passphrase, vowels, special_chars, password_length):
    clean_passphrase = passphrase.strip().lower().replace(' ','')
    output_passphrase_no_numbers = []
    output_passphrase = []
    random_letter = alphabet[random.randint(0, 25)]
    output_passphrase.append(random_letter)
    for i in range(0, len(clean_passphrase)):
        if i % 2 == 0:
            output_passphrase_no_numbers.append(clean_passphrase[i].upper())
        else:
            output_passphrase_no_numbers.append(clean_passphrase[i])
    for i in range(0, len(output_passphrase_no_numbers)):
        if output_passphrase_no_numbers[i] in vowels_as_numbers:
            output_passphrase.append(vowels_as_numbers[output_passphrase_no_numbers[i]])
        else:
            output_passphrase.append(output_passphrase_no_numbers[i])
    while len(output_passphrase) < int(password_length):
        output_passphrase.append(special_characters[random.randint(0, 7)])
    return "".join(output_passphrase)

# Function to estimate how long it would take to crack the passphrase
# assuming 1 billion guesses per second
def crack_time_estimator(password):
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for c in password):
        charset_size += 33
    total_combinations = charset_size ** len(password)
    guesses_per_second = 1000000000
    seconds = total_combinations / guesses_per_second
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    minutes = seconds / 60
    if minutes < 60:
        return f"{minutes:.2f} minutes"
    hours = minutes / 60
    if hours < 24:
        return f"{hours:.2f} hours"
    days = hours / 24
    if days < 365:
        return f"{days:.2f} days"
    years = days / 365
    return f"{years:.2f} years"

# Function to save the original input and generated passphrase to a text file
def save_passphrase_to_file(input_string, passphrase):
    if os.path.exists("passphrase_and_password.txt"):
        with open("passphrase_and_password.txt", "a") as f:
            f.write("\n" + input_string + " : " + passphrase)
        print(f"[+] Added {input_string} and {passphrase} to passphrase_and_password.txt")
        return True
    else:
        with open("passphrase_and_password.txt", "w") as f:
            f.write(input_string + " : " + passphrase)
        print("[+] Created phrase_and_password.txt")
        print(f"[+] Added {input_string} and {passphrase} to passphrase_and_password.txt")
        return True
    
# Small function to check if an input is an integer
def is_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
    
# Greeting function
def greeting():
    print(r"""
************************************************************************************
*  _____  _                        ___  _____                                    _ *
* |  __ \| |                      |__ \|  __ \                                  | |*
* | |__) | |__  _ __ __ _ ___  ___   ) | |__) __ _ ___ _____      _____  _ __ __| |*
* |  ___/| '_ \| '__/ _` / __|/ _ \ / /|  ___/ _` / __/ __\ \ /\ / / _ \| '__/ _` |*
* | |    | | | | | | (_| \__ |  __// /_| |  | (_| \__ \__ \\ V  V | (_) | | | (_| |*
* |_|    |_| |_|_|  \__,_|___/\___|____|_|   \__,_|___|___/ \_/\_/ \___/|_|  \__,_|*
*                                                                                  *
************************************************************************************                                                                                  
          """)
    print("************************************************************************************")
    print("[*] Step 1 : Enter a common, easy to remember phrase!")
    print('[*] Eample: "Please hire me"')
    print("[*] Step 2 : Remove spaces!")
    print("[*] Example: Pleasehireme")
    print("[*] Step 3 : Capitalize every odd-numbered letter in the phrase (i.e 1, 3, 5, etc.)")
    print("[*] Example: PlEaSeHiReMe")
    print("[*] Step 4 : Repleace vowels with numbers!")
    print("[*] Example: Pl34S3H1R3M3")
    print("[*] Step 5 : Add a random letter to the begginning of the password!")
    print("[*] Example: oPlE4S3H1R3M3$#")
    print("[*] Step 6 : Add special characters at the end of the password!")
    print("[*] Example: oPlE4S3H1R3M3$#")
    print('[*] Now you only need to remember "o" + "PlEaSeHiReMe" + "$#"!')
    print("[*]")
    return True


greeting()
input_string = input("[+] Please input an easy to remember phrase: ")
password_length = (input("[+] Please input your desired password length: "))

# Maine Loop
while input_string.lower() != "exit":
    if is_int(password_length) == False:
         print("[!] Password Length must be an integer!")
         password_length = (input("[+] Please input your desired password length: "))
    elif len(input_string.strip().replace(" ", "")) > int(password_length):
        print("[!] Your phrase cannot be longer than your desired password length!")
    elif input_string.strip().replace(" ", "").isalpha() == False:
        print("[!] Your phrase can only contain letters! No punctuation!")
    else:
        new_password = password_generate(input_string, vowels_as_numbers, special_characters, password_length)
        new_password_cracktime = crack_time_estimator(new_password)
        print(f"[+] Your password is {new_password}")
        print(f"[*] It would take {new_password_cracktime} to crack!")
        answer = input("[?] Would you like to save this password? (y/n)")
        if answer.strip() in "yesYES":
            save_passphrase_to_file(input_string, new_password)
    input_string = input("[+] Please input an easy to remember phrase: ")
    if input_string.lower() == "exit":
        sys.exit(0)
    password_length = input("[+] Please input your desired password length: ")
    if password_length.lower() == "exit":
        sys.exit(0)


