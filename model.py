import random 
import string 

def password_generator(length,numbers,special): 
    password = ""
    letters_numbers= string.ascii_letters + string.digits
    letters_special= string.ascii_letters + "!@#$%&?*"  
    all_characters= letters_special + string.digits 
    numbers= numbers.lower()
    special= special.lower()

    if numbers == "false" and special == "false":
        for i in range(length):  
            password += random.choice(string.ascii_letters) 
    elif numbers == "true" and special == "false":
        for i in range(length): 
            password += random.choice(letters_numbers)
    elif numbers == "false" and special == "true":
        for i in range(length):
            password += random.choice(letters_special)   
    elif numbers == "true" and special == "true":
        for i in range(length):
            password += random.choice(all_characters) 
    else:
        print("There is a problem")
        return "There is a problem"
        
    return password 

# def save_password(password):


    
