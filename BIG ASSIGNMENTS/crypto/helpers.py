import string
def alphabet_position(letter):
    return string.ascii_letters.index(letter)
def rotate_character(char, rot): 
    if char.isalpha():
        trans = ""
        big_alf = string.ascii_uppercase
        lil_alf = string.ascii_lowercase
        ind = alphabet_position(char)
        rot += ind 
        if char.isupper():
            if rot > 25:
                rot %= 26
            trans += big_alf[rot]
            return trans
        if char.islower():
            if rot > 25:
                rot %= 26
            trans += lil_alf[rot]
            return trans
    else:
        return char