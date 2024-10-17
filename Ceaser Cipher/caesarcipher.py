
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# FUNCTION CALLED encrypt() THAT TAKE ORIGINAL_TEXT AND SHIFT_AMOUNT AS 2 INPUTS
# INSIDE encrypt() SHIFT EACH LETTER OF ORIGINAL_TEXT FORWARDS IN ALPHABET BY SHIFT_NUMBER AND PRINT ENCRYPTED TEXT
#hello 2
def encrypt(original_text,shift_amount):
    cipher_text="" #j
# WHAT IF U TRY TO SHIFT 'Z' FORWARDS BY 9
    for letter in original_text:
        shifted_position=alphabet.index(letter) + shift_amount #7->9
        shifted_position%=len(alphabet)
        cipher_text+= alphabet[shifted_position] #j
    print(f"Here is the encrypted text: {cipher_text}")
# FUNCTION decrypt() THAT TAKE ORIGINAL_TEXT AND SHIFT_AMOUNT AS 2 INPUTS
# INSIDE encrypt() SHIFT EACH LETTER OF ORIGINAL_TEXT FORWARDS IN ALPHABET BY SHIFT_NUMBER AND PRINT DECRYPTED TEXT
def decrypt(original_text,shift_amount):
    output_text=""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount  # 7->9
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]  # j
    print(f"Here is the decrypted text: {output_text}")
# COMBINE encrypt() &  decrypt() ino ceaser()
def ceaser(original_text,shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        # WHAT IF NUMBER/SYMBOL/SPACE?
        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d text: {output_text}")
#RESTART THE CIPHER PROGRAM
should_continue=True
while should_continue:
    direction: str = input("Type 'encode' to encrypt, type 'decode' to decryp:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

#CALL encrypt()& decrypt() AND PASS INPUTS
# decrypt(original_text=text,shift_amount=shift)
# encrypt(original_text=text,shift_amount=shift)
    ceaser(original_text=text,shift_amount=shift,encode_or_decode=direction)
    restart=input("Type 'yes' if you want to continue.Otherwise type 'no'.\n").lower()
    if restart=="no":
      should_continue=False
      print("Thank you for playing!")