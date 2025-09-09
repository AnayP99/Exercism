def encode(plain_text):
    plain_text = plain_text.replace(" ", "").replace(".", "").replace(",", "").lower()
    result = ""
    for char in plain_text:
        if char.isalpha():
            result +=  chr(219 - ord(char))
        else:
            result += char
    formatted_result = ""
    for i, char in enumerate(result):
        if i!=0 and i%5==0:
            formatted_result+=" "
        formatted_result+=char
    return formatted_result

def decode(ciphered_text):
    ciphered_text = ciphered_text.replace(" ", "")
    result = ""
    for char in ciphered_text:
        if char.isalpha():
            result +=  chr(219 - ord(char))
        else:
            result += char
    return result
