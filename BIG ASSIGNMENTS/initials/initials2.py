def get_initials(fullname):
    name_list = fullname.split()
    initials = ""
    for name in name_list:
        initials += name[0].upper()
    return initials

def main():
    fullname=input("What is your full name?")
    print(fullname)
    print(get_initials(fullname))

if __name__=='__main__':
    main()