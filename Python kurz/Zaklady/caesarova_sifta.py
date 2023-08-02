alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#def encode(message, shift_num):
#    shifted_text =""
#    for i in message:
#        if i != " ":
#            index = alphabet.index(i)
#            new_index = index + shift_num
#            if new_index > 25:
#                new_index %= 26
#            shifted_text += alphabet[new_index]
#        else: shifted_text += i
#    print(shifted_text)
#
#def decode(message, shift_num):
#    shifted_text =""
#    for i in message:
#        if i != " ":
#            index = alphabet.index(i)
#            new_index = index - shift_num
#            if new_index < 0:
#                new_index += 26
#            shifted_text += alphabet[new_index]
#        else: shifted_text += i
#    print(shifted_text)
#
def code(message, shift_num, char):
    shifted_text =""
    for i in message:
        if i != " ":
            index = alphabet.index(i)
            if char == "decode":
                new_index = index - shift_num
                if new_index < 0:
                    new_index += 26
            elif char == "encode":
                new_index = index + shift_num
                if new_index > 25:
                    new_index %= 26
            shifted_text += alphabet[new_index]
        else: shifted_text += i
    print(shifted_text)


want_continue = "yes"
while want_continue == "yes":
    start = input("Type encode or decode:\n").lower()
    word = input("Type your message:\n").lower()
    num = int(input("Type the shift number:\n"))
    code(word, num, start)
    want_continue = input("Chcete pokracovat??\n")
        