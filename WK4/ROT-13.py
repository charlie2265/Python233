from string import ascii_lowercase as lc, ascii_uppercase as uc
# String manipulation
# string.maketrans()
# string.translate()
# lambda
# ROT-13

# This lesson is to emphasize new techniques with built in python methods not security, this is weak encryption

def rot_alpha(n):
    # n is the shift values
    print(lc + uc)      # show the original string
    print(lc[n:] + lc[:n]+ uc[n:] + uc[:n])

    lookup = str.maketrans(lc+uc, lc[n:] + lc[:n]+ uc[n:] + uc[:n])
    print(lookup)

    return lambda s: s.translate(lookup)    #translate characters 1 at a time

val = rot_alpha(10)("At Dawn We Ride")
print("encrypted -> " + val)

decrypted = rot_alpha(10)(val)
print(decrypted)
