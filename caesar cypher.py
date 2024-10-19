


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(otext,stext):
#     ctext = ""

#     for letter in otext:
#         sposition = alphabet.index(letter) + stext
#         sposition %= len(alphabet)
#         ctext += alphabet[sposition]

#     print(f"Here is the encoded result: {ctext}")

# def decrypt(otext,stext):
#     outputtext = ""

#     for letter in otext:
#         sposition = alphabet.index(letter) - stext
#         sposition %= len(alphabet)
#         outputtext += alphabet[sposition]

#     print(f"Here is the encoded result: {outputtext}")

def caesar(otext,stext,encode_or_decode):
    outputtext = ""
    if encode_or_decode == "decode":
        stext *= -1
    for letter in otext:
        if letter not in alphabet:
            outputtext += letter
        else:
            sposition = alphabet.index(letter) + stext
            sposition %= len(alphabet)
            outputtext += alphabet[sposition]                  
    print(f"Here is the {encode_or_decode}d result: {outputtext}")
shouldcontinue = True
while shouldcontinue:
    direction = input("Type 'encode' to encrypt , Type 'decode' to decrypt:\n").lower()
    text = input("Type your massage:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(otext=text , stext=shift ,encode_or_decode=direction)
    restart = input("Typre 'yes' if you want to go again. Otherwise,type 'no'.\n").lower()       
    if restart == "no":
        should_continue = False
        print("Goodbye")




# encrypt(otext = text, stext = shift)
# decrypt(otext = text, stext = shift)