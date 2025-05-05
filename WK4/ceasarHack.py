from string import ascii_lowercase as lc, ascii_uppercase as uc
# character lists
numbers = "0123456789"
spec_char = "!@$%^&*()?/|"
base_str = lc + uc + numbers + spec_char + " "

def split(word):
    return [char for char in word] 
base_list = split(base_str)
print(base_list)

def ceasar(message, shift):
    myCode = str("")
    for chara in message:
        msgPos = base_list.index(chara)
        shftPos = msgPos + shift

        if shftPos >= 75:
            shftPos -= 76
        myCode = myCode + base_list[shftPos]


    print(myCode)

for c in range(77):
    ceasar("@topGtoIGpKtAxCvo2368WopIo)?oBEwb", c)






# decrypt = str("")
# for chara in encrypted:
#     msgPos = codeList.index(chara)
#     shftPos = msgPos - shift

#     # as soon as shftPos goes above 26 (27)
#     # subtract 27. making shftPos 0
#     if shftPos < 0:
#         shftPos += 27
#     decrypt = decrypt + codeList[shftPos]
    
# print(decrypt)


# determine index position of the letter
# determine new letter at the shifted position
# create the encrypted message letter-by-letter
