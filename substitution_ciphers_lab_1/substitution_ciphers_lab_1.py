from itertools import permutations

'''
Function to decrypt a string

@param {string} user_string - string that user enters to be decrypted
@param {set} word_set - set of words from english_words.txt
'''
def word_decrypt(user_string, word_set):
    #first check for cesear decryption since it is the quickest one to check
    MAX_ROT = 26

    #take out the white spaces of the string
    user_string = user_string.lower().replace(" ","")
    # Change the string into a list to work with the characters easier
    string_list = list(user_string)

    #Implement a rotation
    for rotation_num in range (MAX_ROT):
        initial_char_check = 20 # Number of characters checked to determine if check should continue
        threshold_percent = .3 # Precent of 4 letter words in the paragraph to make it a real sentence
        string_list = list(user_string)

        # Use ASCII code to rotate the letters 97-122
        for i in range (len(string_list)):
            # Reset the ASCII after the letter 'z'
            if (ord(string_list[i]) + rotation_num > 122):
                string_list[i] = (chr(ord(string_list[i]) + rotation_num - 26));
            else:
                string_list[i] = (chr(ord(string_list[i]) + rotation_num));
        string_list = "".join(string_list)

        if(check_string(string_list, initial_char_check, 3, word_set) > 0):
            # Checking for the percent of n number of letters to determine if it is a real sentence
            # Check percentages because this program cannot split words yet
            if (float(check_string(string_list, len(string_list), 3, word_set) * 3 / len(string_list)) > threshold_percent or
                float(check_string(string_list, len(string_list), 4, word_set) * 4 / len(string_list)) > threshold_percent or 
                float(check_string(string_list, len(string_list), 5, word_set) * 5 / len(string_list)) > threshold_percent):
                print(string_list)
        
    # Next check for substitution encryption

'''
Input a string to check if it is a real sentence

@param {string} string - string that is going to be checked
@param {int} string_length_check - the amount of chars from the beginning that will be checked. Must be greater than char_length_check
@param {set} word_set - set of words from english_words.txt

@return {int} - returns the number of real english word that was detected
'''
def check_string(string, string_length_check, char_length_check, word_set):
    real_word_counter = 0 # Counter to see how many words in the sentence are real
    check_string = string[:string_length_check]

    for i in range (string_length_check - char_length_check):
        if (check_word(string[i:i + char_length_check], word_set) == True):
            real_word_counter += 1
    return real_word_counter

'''
Gets all the possible permutation of a string

@param {list} lst - takes in a list of characters to get all the possible permutations

@return {list} - returns the list of possible permutations
'''

def permutation(lst):
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are more than 1 characters 
    l = [] # empty list that will store current permutation 
    print(l)
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
        m = lst[i] 
  
        # Extract lst[i] or m from the list. remLst is remaining list
 
        remLst = lst[:i] + lst[i+1:] 
  
        # Generating all permutations where m is first element  
        for p in permutation(remLst): 
            l.append([m] + p) 
    return l 

'''
Input a word to check if it exist in the list of words

@param {string} word - word that is going to be check against a list of english words
@param {set} word_set - set of words from english_words.txt

@return {boolean} - returns a true boolean if the word is contained in the set. If not, returns false
'''
def check_word(word, word_set):
    return word in word_set

    
'''
Load the words from english_words.txt and puts everything into a set for easy search
'''
def load_words():
    with open('english_words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


# Strings to use
'''
1. fqjcb rwjwj  vnjax  bnkhj  whxcq  nawjv  nfxdu  mbvnu  ujbbf  nnc

2. oczmz  vmzor  jocdi  bnojv  dhvod  igdaz  admno  ojbzo  rcvot  jprvi  oviyv aozmo cvooj  ziejt  dojig  toczr  dnzno  jahvi  fdiyv  xcdzq  zoczn  zxjiy

3. ejitp  spawa  qleji  taiul  rtwll  rflrl  laoat  wsqqj  atgac  kthls  iraoatwlpl qjatw  jufrh  lhuts  qataq  itats  aittk  stqfj  cae

4. iyhqz  ewqin  azqej  shayz  niqbe  aheum  hnmnj  jaqii  yuexq  ayqkn  jbeuqiihed yzhni  ifnun  sayiz  yudhe  sqshu  qesqa  iluym  qkque  aqaqm  oejjshqzyu  jdzqa diesh  niznj  jayzy  uiqhq  vayzq  shsnj  jejjz  nshna  hnmytisnae  sqfun  dqzew qiead  zevqi  zhnjq  shqze  udqai  jrmtq  uishq  ifnunsiiqa  suoij  qqfni  syyle iszhn  bhmei  squih  nimnx  hsead  shqmr  udquq uaqeu  iisqe  jshnj  oihyy  snaxs hqihe  lsilu  ymhni  tyz
'''

#Prompt the user to enter in the string they want to use
#print("Enter in the string to decrypt")
#user_string = input()

## Load word from text document
#english_words = load_words()
#word_decrypt(user_string, english_words)
yes = list('ABCD')
permutation(yes)