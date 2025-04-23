# phrase2password
 Passphrase-Based Password Generator: Takes an inputted phrase and generates an easy-to-remember but complex password.


## Description

This script generates a strong password based on a user-provided passphrase. It applies a series of transformations to the passphrase to create a complex password and estimates the time it would take to crack it using a brute-force approach.

### How to Use





- Ensure you have Python installed on your system (I used Python 3.13.3 for this project).



- Save the script as phrase2password.py (or any name you prefer).



- Run the script from the command line: python phrase2password.py.


- Follow the prompts:





  - Enter an easy-to-remember passphrase (e.g., "Please hire me").



  - Enter the desired password length (must be an integer).



- The script will generate a password, display it along with an estimated crack time, and ask if you want to save the passphrase and password to a file named passphrase_and_password.txt.

## Transformation Steps

The script transforms the passphrase through the following steps:





- Clean the passphrase: Remove spaces and convert to lowercase (e.g., "Please hire me" → "pleasehireme").



- Capitalize every other letter: Starting with the first letter (e.g., "pleasehireme" → "PlEaSeHiReMe").



- Replace vowels with numbers: Replace 'a' with '4', 'e' with '3', 'i' with '1', 'o' with '0' (e.g., "PlEaSeHiReMe" → "Pl34S3H1R3M3").



- Add a random letter at the beginning: Choose a random lowercase letter (e.g., "dPl34S3H1R3M3").



- Append special characters: Add random special characters until the password reaches the desired length (e.g., "dPl34S3H1R3M3@!").

### Crack Time Estimation

The script estimates the time it would take to crack the password using a brute-force attack, assuming 1 billion guesses per second. The estimation is based on the character set used in the password.


#### Notes





- The passphrase should contain only letters (no numbers or special characters).



- The desired password length must be an integer and should be greater than or equal to the length of the transformed passphrase.



- The generated password and the original passphrase can be saved to a file for future reference.
- This program uses the MIT license and is free for anybody who wants to use it or modify it. 
