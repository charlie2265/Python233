'''Multiplicative cyphor Demo'''
base_list = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
base_list.append(" ")

def multiplicative(message, key):
    encrypt = str(" ")
    
    # table headers for testing table
    # print(f"Key: {key}")
    # print("Plain \tPos \tNew \tEnc")
    # print("Car\t \tPos \tChar")
    # print("-" * 30)

    for character in message:
        pos = base_list.index(character)

        # encryption
        new_pos = (pos * key) % 27
        encrypt = encrypt + base_list[new_pos]
        # print testing table
        # print(f"{base_list[pos]} \t{pos} \t{new_pos} \t{base_list[new_pos]}")

    return encrypt
encrypted = "AZUVATKUTBULCVB"
message = "AT DAWN WE RIDE"
print("First Message>> ", encrypted)
encrypt_message = multiplicative(encrypted, 4)
print("encrypted Message>>", encrypt_message)
