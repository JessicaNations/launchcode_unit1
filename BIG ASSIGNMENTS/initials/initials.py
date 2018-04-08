def get_initials(fullname):
    name_list = fullname.split()
    initials = ""
    for name in name_list:
        initials += name[0].upper()
    return initials

def main():
    print(get_initials("harry potter"))
    print(get_initials("daniel Day lewis"))
    print(get_initials("lawonda smith"))

if __name__=='__main__':
    main()
