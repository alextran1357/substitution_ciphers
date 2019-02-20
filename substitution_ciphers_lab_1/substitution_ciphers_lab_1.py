#Function to decrypt a string
def word_decrypt(user_string):
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
            if (ord(string_list[i]) + rotation_num > 122):
                string_list[i] = (chr(ord(string_list[i]) + rotation_num - 26));
            else:
                string_list[i] = (chr(ord(string_list[i]) + rotation_num));
        string_list = "".join(string_list)
        print(string_list)
    
# Strings to use
'''
1. fqjcb rwjwj  vnjax  bnkhj  whxcq  nawjv  nfxdu  mbvnu  ujbbf  nnc

2. oczmz  vmzor  jocdi  bnojv  dhvod  igdaz  admno  ojbzo  rcvot  jprvi  oviyv aozmo cvooj  ziejt  dojig  toczr  dnzno  jahvi  fdiyv  xcdzq  zoczn  zxjiy

3. ejitp  spawa  qleji  taiul  rtwll  rflrl  laoat  wsqqj  atgac  kthls  iraoatwlpl qjatw  jufrh  lhuts  qataq  itats  aittk  stqfj  cae

4. iyhqz  ewqin  azqej  shayz  niqbe  aheum  hnmnj  jaqii  yuexq  ayqkn  jbeuqiihed yzhni  ifnun  sayiz  yudhe  sqshu  qesqa  iluym  qkque  aqaqm  oejjshqzyu  jdzqa diesh  niznj  jayzy  uiqhq  vayzq  shsnj  jejjz  nshna  hnmytisnae  sqfun  dqzew qiead  zevqi  zhnjq  shqze  udqai  jrmtq  uishq  ifnunsiiqa  suoij  qqfni  syyle iszhn  bhmei  squih  nimnx  hsead  shqmr  udquq uaqeu  iisqe  jshnj  oihyy  snaxs hqihe  lsilu  ymhni  tyz
'''

#Prompt the user to enter in the string they want to use
print("Enter in the string to decrypt")
user_string = input()

word_decrypt(user_string)