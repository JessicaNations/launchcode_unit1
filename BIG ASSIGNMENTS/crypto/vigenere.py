from helpers import alphabet_position, rotate_character
def encrypt(text, key):
    trans = []
    start_ind = 0
    for i in text:
        if i.isalpha() == False:
            start_ind -= 1
        key_int = alphabet_position(key[start_ind]) 
        trans.append(rotate_character(i, key_int)) 
        if start_ind == (len(key)-1): 
            start_ind = 0  
        else:
            start_ind += 1 
            
    return "".join(trans)
def main():
    text = input("Type a message:")
    key = input("Encryption key:")
    print(encrypt(text, key))
if __name__=="__main__":
    main()