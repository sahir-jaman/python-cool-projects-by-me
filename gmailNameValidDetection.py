email = "sahir2@gmail.com"

size1 = len(email)-10
size2 = len(email)-1


def lastPartMatching(size1, size2, email):
    matching = ""
    for i in range(size1, size2 + 1):
        matching += email[i]
    if matching == "@gmail.com":
        return True
    else:
        return False


def isSpaceAndBadCharecter(email):
    flag1, flag2 = 0, 0
    for i in email:
        if i.isalpha():
            if i.isupper():
                flag1 = 1
            else:
                continue
        elif i.isdigit():
            continue
        elif i == '_' or i == '.' or i == '@':
            continue
        else:
            flag2 = 1
    if flag1 == 1 or flag2 ==1:
        return True
    else:
        return False


if len(email)>=11:
    if email[0].isalpha():
        if email[size1-1].isalpha() or email[size1-1].isnumeric():
            if lastPartMatching(size1,size2,email):
                if isSpaceAndBadCharecter(email):
                    print("Your Email is Wrong :( ")
                else:
                    print("Your Email is valid :) ")
            else:
                print("Your Email is Wrong :( ")
        else:
            print("Your Email is Wrong :( ")
    else:
        print("Your Email is Wrong :( ")
else:
    print("Your Email is Wrong :( ")
