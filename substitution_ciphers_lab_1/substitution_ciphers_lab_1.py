'''
Function to decrypt a string

@param {string} user_string - string that user enters to be decrypted
@param {set} word_set - set of words from english_words.txt
'''
def word_decrypt(user_string, word_set):
    #first check for cesear decryption
    MAX_ROT = 26

    #take out the white spaces of the string
    user_string = user_string.lower().replace(" ","")
    # Change the string into a list to work with the characters easier
    string_list = list(user_string)

    #Implement a rotation
    for rotation_num in range (MAX_ROT):
        string_list = list(user_string)
        # Use ASCII code to rotate the letters 97-122
        for i in range (len(string_list)):
            # Reset the ASCII after the letter 'z'
            if (ord(string_list[i]) + rotation_num > 122):
                string_list[i] = (chr(ord(string_list[i]) + rotation_num - 26));
            else:
                string_list[i] = (chr(ord(string_list[i]) + rotation_num));
        string_list = "".join(string_list)
        print(string_list)

'''
Input a string to check if it is a real sentence

@param {string} string - string that is going to be checked
@param {int} string_length_check - the amount of chars from the beginning that will be checked. Must be greater than char_check_length
@param {int} char_check_length - the number of characters checked to see if it is an english word; either 4 or 5 which are most common
@param {set} word_set - set of words from english_words.txt
'''
def check_string(string, string_length_check, char_check_length, word_set):
    check_string = string[:string_length_check]
    for i in range (string_length_check - char_check_length):
       check_word(string[i:i + char_check_length])
    

'''
Input a word to check if it exist in the list of words

@param {string} word - word that is going to be check against a list of english words
@param {set} word_set - set of words from english_words.txt
'''
def check_word(word, word_set):
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  We can use binary search for quicker searching  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    print("Hello")

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
print("Enter in the string to decrypt")
#user_string = input()
english_words = load_words()
#word_decrypt(user_string)
check_string("hellhellehhellehehehe", 10, 4)