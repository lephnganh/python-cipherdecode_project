#Decoding Ceasar Cipher:
message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
translated = ""
for letter in message:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        translated += alphabet[(letter_value + 10) % 26]
    else:
        translated += letter
#print(translated)

reply = "ok haha dumbass!!??"
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
coded = ""
for letter in reply:
    if not letter in punctuation:
        letter_value = alphabet.find(letter)
        coded += alphabet[(letter_value - 10) % 26]
    else:
        coded += letter
#print(coded)

reply1 = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
reply2 = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

def decoder (message, offset):
    output = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            output += alphabet[(letter_value + offset) % 26]
        else:
            output += letter
    return output

def coder (message, offset):
    output = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            output += alphabet[(letter_value - offset) % 26]
        else:
            output += letter
    return output

#print(decoder(reply1, 10))
#print(decoder(reply2, 14))

reply3 = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
#for i in range(0,26):
    #print("with offset =",  str(i), decoder(reply3, i))
#print(decoder(reply3, 7))


#Decoding The Vigenère Cipher
message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

def decode(message, keyword):
    letter_index = 0
    ori_keyword = ""
    for i in range(0, len(message)):
        if message[i] in punctuation:
            ori_keyword += message[i]
        else:
            ori_keyword += keyword[letter_index]
            letter_index = (letter_index + 1) % len(keyword)
    translated = ""
    for i in range(0, len(message)):
        if not message[i] in punctuation:
            ln = alphabet.find(message[i]) - alphabet.find(ori_keyword[i])
            translated += alphabet[ln % 26]
        else:
            translated += message[i]
    return translated

print(decode(message, keyword))



