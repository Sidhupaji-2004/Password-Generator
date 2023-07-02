'''

Random Password Generator using python
Author : Siddharth Sen

'''

import random
import string # importing two libraries for this project : random and string. 


print("Welcome to Password Generator. How can we help you ? ")
password_length = int(input("Enter the length of the password to be generated \n"))
"""
    using the string module to concatenate all the data including : 

        uppercase characters
        lowercase characters
        numbers
        whitespace
        punctuations / symbols
    and storing them in the all_data variable. 

"""
all_data = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation + string.whitespace

"""
random .sample has a unique feature: 
    random.sample() does not repeat characters and selects the required no. of characters
"""
generated_password = random.sample(all_data, password_length)
# generated_password = "".join(temp_string)
# why can't temp_String itself be used as the generated password
print("The generated password is: \n")
print(generated_password)

