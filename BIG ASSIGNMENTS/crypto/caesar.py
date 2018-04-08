from helpers import alphabet_position, rotate_character
def encrypt(text, rot):
    new_text = ""
    for i in text:
        new_text += rotate_character(i, rot)
    return "".join(new_text)
def main():
    text = input("Type a message:")
    rot = input("Encryption rotation:")
    rot = int(rot)
    print(encrypt(text, rot))
if __name__=="__main__":
    main()