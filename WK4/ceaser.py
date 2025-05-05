# base list convert string to list using .split()
base_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" .split()
print(base_list)
base_list.append(" ")
print(base_list)
# message
message = "AT DAWN WE RIDE"

# shift
shift = 3

#---- create a loop ----#
# take each letter of the message
encrypted  =  str("")
for chara in message:
    msgPos = base_list.index(chara)
    shftPos = msgPos + shift

    # as soon as shftPos goes above 26 (27)
    # subtract 27. making shftPos 0
    if shftPos >= 26:
        shftPos -= 27

    # print(f"Character {chara} is {base_list[shftPos]}")

    encrypted = encrypted +base_list[shftPos]

print(encrypted)

decrypt = str("")
for chara in encrypted:
    msgPos = base_list.index(chara)
    shftPos = msgPos - shift

    # as soon as shftPos goes above 26 (27)
    # subtract 27. making shftPos 0
    if shftPos < 0:
        shftPos += 27
    decrypt = decrypt + base_list[shftPos]
    
print(decrypt)


# determine index position of the letter
# determine new letter at the shifted position
# create the encrypted message letter-by-letter