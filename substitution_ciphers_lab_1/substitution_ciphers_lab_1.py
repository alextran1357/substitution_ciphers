#Function to decrypt a string
def word_decrypt(user_string):
    #first check for cesear decryption
    MAX_ROT = 25 #25 because 26 would just loop in another check

    #take out the white spaces of the string
    user_string = user_string.lower().replace(" ","")
    #print(user_string)
    

#Prompt the user to enter in the string they want to use
print("Enter in the string to decrypt")
user_string = input()

word_decrypt(user_string)